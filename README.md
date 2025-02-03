Sequence of evictions doesn't match the sequence of LRU:
![alt text](image.png)

![alt text](image-3.png)

```
root@900c69d5ad3d:/scripts# bash ./load_test.sh 

{       "transactions":                          100,
        "availability":                       100.00,
        "elapsed_time":                         5.11,
        "data_transferred":                     0.00,
        "response_time":                        0.51,
        "transaction_rate":                    19.57,
        "throughput":                           0.00,
        "concurrency":                          9.96,
        "successful_transactions":               100,
        "failed_transactions":                     0,
        "longest_transaction":                  0.52,
        "shortest_transaction":                 0.50
}
```

