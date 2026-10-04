import heapq

results = [
    ("model_A", 0.81),
    ("model_B", 0.73),
    ("model_A", 0.85),
    ("model_C", 0.91),
    ("model_B", 0.78),
]

k = 2


def top_k_scores_naive(results, k):
    model_top_k = {}

    for model, score in results:
        if model not in model_top_k:
            model_top_k[model] = [score]
        elif len(model_top_k[model]) < k:
            model_top_k[model].append(score)
        elif model_top_k[model][-1] < score:
            model_top_k[model][-1] = score

        model_top_k[model] = sorted(model_top_k[model], reverse=True)

    return model_top_k


def top_k_scores_heap(results, k):
    model_top_k = {}

    for model, score in results:
        if model not in model_top_k:
            model_top_k[model] = [score]
        elif len(model_top_k[model]) < k:
            heapq.heappush(model_top_k[model], score)
        else:
            heapq.heappushpop(model_top_k[model], score)

    return model_top_k


naive_result = top_k_scores_naive(results, k)
heap_result = top_k_scores_heap(results, k)

print("Naive:")
print(naive_result)

print("\nHeap:")
print(heap_result)

print("\nHeap sorted:")
print({
    model: sorted(scores, reverse=True)
    for model, scores in heap_result.items()
})
