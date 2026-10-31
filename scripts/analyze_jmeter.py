import argparse
import csv
import statistics
from collections import defaultdict
from pathlib import Path


def percentile(values, percentile_value):
    if not values:
        return 0.0
    ordered = sorted(values)
    rank = max(0, (len(ordered) - 1) * percentile_value)
    lower = int(rank)
    upper = min(lower + 1, len(ordered) - 1)
    fraction = rank - lower
    return ordered[lower] + (ordered[upper] - ordered[lower]) * fraction


def analyze(path):
    samples_by_label = defaultdict(list)
    failures_by_label = defaultdict(int)

    with Path(path).open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        required = {"elapsed", "label", "success"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("JTL must contain elapsed, label, and success columns")

        for row in reader:
            elapsed = float(row["elapsed"])
            label = row["label"] or "(unlabelled)"
            samples_by_label[label].append(elapsed)
            if row["success"].strip().lower() != "true":
                failures_by_label[label] += 1

    results = {}
    total_samples = 0
    total_failures = 0
    for label, values in samples_by_label.items():
        failures = failures_by_label[label]
        count = len(values)
        total_samples += count
        total_failures += failures
        results[label] = {
            "samples": count,
            "average_ms": round(statistics.fmean(values), 2),
            "p95_ms": round(percentile(values, 0.95), 2),
            "max_ms": round(max(values), 2),
            "error_rate_pct": round(failures * 100 / count, 2),
        }
    overall_error_rate = total_failures * 100 / total_samples if total_samples else 0.0
    return results, total_samples, round(overall_error_rate, 2)


def main():
    parser = argparse.ArgumentParser(description="Summarize a JMeter JTL result file")
    parser.add_argument("jtl", nargs="?", default="jmeter/results.jtl")
    parser.add_argument("--max-p95-ms", type=float)
    parser.add_argument("--max-error-rate-pct", type=float)
    args = parser.parse_args()

    results, total_samples, error_rate = analyze(args.jtl)
    print(f"samples={total_samples} overall_error_rate_pct={error_rate}")
    for label in sorted(results):
        metrics = results[label]
        print(
            f"{label}: samples={metrics['samples']} average_ms={metrics['average_ms']} "
            f"p95_ms={metrics['p95_ms']} max_ms={metrics['max_ms']} "
            f"error_rate_pct={metrics['error_rate_pct']}"
        )

    if args.max_p95_ms is not None:
        breaches = [label for label, metrics in results.items() if metrics["p95_ms"] > args.max_p95_ms]
        if breaches:
            parser.error("p95 threshold exceeded: " + ", ".join(breaches))
    if args.max_error_rate_pct is not None and error_rate > args.max_error_rate_pct:
        parser.error(f"overall error-rate threshold exceeded: {error_rate}%")


if __name__ == "__main__":
    main()
