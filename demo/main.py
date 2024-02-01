import sys
sys.path.append("../")

from deeploglizer.common.dataloader import load_HDFS

train_data, test_data = load_HDFS(
    log_file = "../data/HDFS/HDFS_100k.log_structured.csv",
    label_file = "../data/HDFS/anomaly_label.csv",
    train_ratio = 0.8,
    test_ratio = 0.2,
    train_anomaly_ratio = 0.5,
    random_partition = True
)

for session_id, session_info in list(train_data.items())[:1]:
    print(f"Session ID: {session_id}, Label: {session_info['label']}")
    print("Templates:", session_info['templates'])
