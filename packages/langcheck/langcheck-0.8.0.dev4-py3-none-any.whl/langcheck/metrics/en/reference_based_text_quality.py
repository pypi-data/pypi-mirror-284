from __future__ import annotations

from typing import List, Optional

from rouge_score import rouge_scorer

from langcheck.metrics._validation import (
    validate_parameters_answer_correctness,
    validate_parameters_reference_based,
)
from langcheck.metrics.eval_clients import EvalClient, load_prompt_template
from langcheck.metrics.metric_value import MetricValue
from langcheck.metrics.scorer.hf_models import (
    SentenceTransformerSimilarityScorer,
)
from langcheck.utils.progess_bar import tqdm_wrapper


def answer_correctness(
    generated_outputs: List[str] | str,
    reference_outputs: List[str] | str,
    prompts: List[str] | str,
    eval_model: EvalClient,
) -> MetricValue[Optional[float]]:
    """Calculates the correctness of the generated outputs. This metric takes on
    float values of either 0.0 (Incorrect), 0.5 (Partially Correct), or 1.0
    (Correct). The score may also be `None` if it could not be computed.

    We currently only support the evaluation based on an EvalClient.

    Args:
        generated_outputs: The model generated output(s) to evaluate
        reference_outputs: The reference output(s)
        prompts: The prompts used to generate the output(s)
        eval_model: The EvalClient instance used for the evaluation

    Returns:
        A :class:`~langcheck.metrics.metric_value.MetricValue` object
    """
    generated_outputs, reference_outputs, prompts = (
        validate_parameters_answer_correctness(
            generated_outputs, reference_outputs, prompts
        )
    )

    answer_correctness_template = load_prompt_template(
        language="en", eval_client=eval_model, metric_name="answer_correctness"
    )

    populated_prompts = [
        answer_correctness_template.render(
            {"gen_output": gen_output, "ref_output": ref, "user_query": prompt}
        )
        for gen_output, ref, prompt in zip(
            generated_outputs, reference_outputs, prompts
        )
    ]

    scores, explanations = eval_model.get_score(
        metric_name="answer correctness",
        language="en",
        prompts=populated_prompts,
        score_map={"Correct": 1.0, "Partially Correct": 0.5, "Incorrect": 0.0},
    )

    return MetricValue(
        metric_name="answer_correctness",
        prompts=prompts,
        generated_outputs=generated_outputs,
        reference_outputs=reference_outputs,
        sources=None,
        explanations=explanations,
        metric_values=scores,
        language="en",
    )


def semantic_similarity(
    generated_outputs: List[str] | str,
    reference_outputs: List[str] | str,
    prompts: Optional[List[str] | str] = None,
    eval_model: str | EvalClient = "local",
) -> MetricValue[float]:
    """Calculates the semantic similarities between the generated outputs and
    the reference outputs. The similarities are computed as the cosine
    similarities between the generated and reference embeddings. This metric
    takes on float values between [-1, 1], but typically ranges between 0 and 1
    where 0 is minimum similarity and 1 is maximum similarity.

    We currently support two embedding model types:

    1. The 'local' type, where the 'all-mpnet-base-v2' model is downloaded
    from HuggingFace and run locally. This is the default model type and
    there is no setup needed to run this.

    2. The EvalClient type, where you can use a similarlity scorer returned by
    the given EvalClient. The scorer is typically implemented using the
    embedding APIs of cloud services. The implementation details are explained
    in each of the concrete EvalClient classes.

    Ref:
        https://huggingface.co/tasks/sentence-similarity
        https://www.sbert.net/docs/usage/semantic_textual_similarity.html

    Args:
        generated_outputs: The model generated output(s) to evaluate
        reference_outputs: The reference output(s)
        prompts: The prompts used to generate the output(s). Prompts are
            optional metadata and not used to calculate the metric.
        eval_model: The type of model to use ('local' or the EvalClient instance
            used for the evaluation). default 'local'

    Returns:
        An :class:`~langcheck.metrics.metric_value.MetricValue` object
    """
    generated_outputs, reference_outputs, prompts = (
        validate_parameters_reference_based(
            generated_outputs, reference_outputs, prompts
        )
    )
    if eval_model == "local":
        scorer = SentenceTransformerSimilarityScorer(language="en")
    else:  # EvalClient
        assert isinstance(
            eval_model, EvalClient
        ), "An EvalClient must be provided for non-local model types."
        scorer = eval_model.similarity_scorer()

    scores = scorer.score(generated_outputs, reference_outputs)
    return MetricValue(
        metric_name="semantic_similarity",
        prompts=prompts,
        generated_outputs=generated_outputs,
        reference_outputs=reference_outputs,
        sources=None,
        explanations=None,
        metric_values=scores,
        language="en",
    )


def rouge1(
    generated_outputs: List[str] | str,
    reference_outputs: List[str] | str,
    prompts: Optional[List[str] | str] = None,
) -> MetricValue[float]:
    """Calculates the F1 metrics of the ROUGE-1 scores between the generated
    outputs and the reference outputs. It evaluates the overlap of unigrams
    (single tokens) between the generated outputs and the reference outputs.
    This metric takes on float values between [0, 1], where 0 is no overlap and
    1 is complete overlap.

    Ref:
        https://github.com/google-research/google-research/tree/master/rouge

    Args:
        generated_outputs: The model generated output(s) to evaluate
        reference_outputs: The reference output(s)
        prompts: The prompts used to generate the output(s). Prompts are
            optional metadata and not used to calculate the metric.

    Returns:
        An :class:`~langcheck.metrics.metric_value.MetricValue` object
    """
    generated_outputs, reference_outputs, prompts = (
        validate_parameters_reference_based(
            generated_outputs, reference_outputs, prompts
        )
    )

    scores = _rouge(generated_outputs, reference_outputs, "rouge1")
    return MetricValue(
        metric_name="rouge1",
        prompts=prompts,
        generated_outputs=generated_outputs,
        reference_outputs=reference_outputs,
        sources=None,
        explanations=None,
        metric_values=scores,
        language="en",
    )


def rouge2(
    generated_outputs: List[str] | str,
    reference_outputs: List[str] | str,
    prompts: Optional[List[str] | str] = None,
) -> MetricValue[float]:
    """Calculates the F1 metrics of the ROUGE-2 scores between the generated
    outputs and the reference outputs. It evaluates the overlap of bigrams
    (two adjacent tokens) between the generated outputs and the reference
    outputs. This metric takes on float values between [0, 1], where 0 is no
    overlap and 1 is complete overlap.

    Ref:
        https://github.com/google-research/google-research/tree/master/rouge

    Args:
        generated_outputs: The model generated output(s) to evaluate
        reference_outputs: The reference output(s)
        prompts: The prompts used to generate the output(s). Prompts are
            optional metadata and not used to calculate the metric.

    Returns:
        An :class:`~langcheck.metrics.metric_value.MetricValue` object
    """
    generated_outputs, reference_outputs, prompts = (
        validate_parameters_reference_based(
            generated_outputs, reference_outputs, prompts
        )
    )

    scores = _rouge(generated_outputs, reference_outputs, "rouge2")
    return MetricValue(
        metric_name="rouge2",
        prompts=prompts,
        generated_outputs=generated_outputs,
        reference_outputs=reference_outputs,
        sources=None,
        explanations=None,
        metric_values=scores,
        language="en",
    )


def rougeL(
    generated_outputs: List[str] | str,
    reference_outputs: List[str] | str,
    prompts: Optional[List[str] | str] = None,
) -> MetricValue[float]:
    """Calculates the F1 metrics of the ROUGE-L scores between the generated
    outputs and the reference outputs. It evaluates the longest common
    subsequence (LCS) between the generated outputs and the reference outputs.
    This metric takes on float values between [0, 1], where 0 means that the LCS
    is empty and 1 means that the reference and generated outputs are the same.

    Ref:
        https://github.com/google-research/google-research/tree/master/rouge

    Args:
        generated_outputs: The model generated output(s) to evaluate
        reference_outputs: The reference output(s)
        prompts: The prompts used to generate the output(s). Prompts are
            optional metadata and not used to calculate the metric.

    Returns:
        An :class:`~langcheck.metrics.metric_value.MetricValue` object
    """
    generated_outputs, reference_outputs, prompts = (
        validate_parameters_reference_based(
            generated_outputs, reference_outputs, prompts
        )
    )

    # The `rouge_score` package has two flavors of ROUGE-L [1]:
    # - 1) sentence-level, where newline characters are ignored
    # - 2) summary-level, where newline characters are interpreted as sentence
    #      boundaries
    #
    # We use (2) here (i.e. `rougeLsum`) because this is how `pyrouge` computes
    # the ROUGE-L score (https://github.com/bheinzerling/pyrouge), which is a
    # Python wrapper around original perl script implementation.
    #
    # [1] https://github.com/google-research/google-research/tree/master/rouge#two-flavors-of-rouge-l
    scores = _rouge(generated_outputs, reference_outputs, "rougeLsum")
    return MetricValue(
        metric_name="rougeL",
        prompts=prompts,
        generated_outputs=generated_outputs,
        reference_outputs=reference_outputs,
        sources=None,
        explanations=None,
        metric_values=scores,
        language="en",
    )


def _rouge(
    generated_outputs: List[str], reference_outputs: List[str], rouge_type: str
) -> List[float]:
    """Helper function for computing the rouge1, rouge2, and rougeL metrics.
    This uses Google Research's implementation of ROUGE:
    https://github.com/google-research/google-research/tree/master/rouge

    Args:
        generated_outputs: A list of model generated outputs to evaluate
        reference_outputs: A list of reference outputs
        rouge_type: rouge1, rouge2, or rougeLsum

    Returns:
        A list of F1 values of the ROUGE scores
    """
    assert rouge_type in ["rouge1", "rouge2", "rougeLsum"]
    scorer = rouge_scorer.RougeScorer([rouge_type], use_stemmer=True)
    scores = []
    for gen, ref in tqdm_wrapper(
        zip(generated_outputs, reference_outputs), total=len(generated_outputs)
    ):
        score = scorer.score(gen, ref)
        scores.append(score[rouge_type].fmeasure)
    return scores
