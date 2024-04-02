from commons.evaluation import calculate_metrics


def test_evaluate_metrics_1():
    fn = {'a': [{"expected": ["aa"], "predicted": ["ba"]}], 'b': []}
    fp = {'a': [{"expected": ["aa"], "predicted": ["ba"]}], 'b': []}
    tp = {'a': [], 'b': [{"expected": ["aa"], "predicted": ["ba"]}, {"expected": ["aa"], "predicted": ["ba"]},
                         {"expected": ["aa"], "predicted": ["ba"]}]}

    precision_micro_avg, recall_micro_avg, f1_score_micro_avg, precision_macro_avg, recall_macro_avg, f1_score_macro_avg = calculate_metrics(
        tp=tp, fp=fp, fn=fn)

    assert precision_micro_avg == 3 / (3 + 1)
    assert precision_macro_avg == (0 + 1) / 2

    assert recall_micro_avg == 3 / (3 + 1)
    assert recall_macro_avg == (0 + 1) / 2
