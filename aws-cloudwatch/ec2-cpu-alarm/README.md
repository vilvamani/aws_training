## AWS CloudWatch Alarm to Monitor CPU Utilization

You can monitor your AWS EC2 CPU Utilization by using Amazon CloudWatch.

## Setting Up a CPU Usage Alarm Using the AWS Management Console

1. Open the CloudWatch console at https://console.aws.amazon.com/cloudwatch/.

2. In the navigation pane, choose Alarms, Create Alarm.

3. Choose Select metric.

4. In the All metrics tab, choose EC2 metrics.

5. Choose a metric category (for example, Per-Instance Metrics).

6. Find the row with the instance that you want listed in the InstanceId column and CPUUtilization in the Metric Name column. Select the check box next to this row, and choose Select metric.

7. Under Specify metric and conditions, for Statistic choose Average, choose one of the predefined percentiles, or specify a custom percentile (for example, p95.45).

8. Choose a period (for example, 5 minutes).

9. Under Conditions, specify the following:

    a. For Threshold type, choose Static.

    b. For Whenever CPUUtilization is, specify Greater. Under than..., specify the threshold that is to trigger the alarm to go to ALARM state if the CPU utilization exceeds this percentage. For example, 70.

    c. Choose Additional configuration. For Datapoints to alarm, specify how many evaluation periods (data points) must be in the ALARM state to trigger the alarm. If the two values here match, you create an alarm that goes to ALARM state if that many consecutive periods are breaching.

    To create an M out of N alarm, specify a lower number for the first value than you specify for the second value. For more information, see Evaluating an Alarm.

    d. For Missing data treatment, choose how to have the alarm behave when some data points are missing. For more information, see Configuring How CloudWatch Alarms Treat Missing Data.

    e. If the alarm uses a percentile as the monitored statistic, a Percentiles with low samples box appears. Use it to choose whether to evaluate or ignore cases with low sample rates. If you choose ignore (maintain alarm state), the current alarm state is always maintained when the sample size is too low. For more information, see Percentile-Based CloudWatch Alarms and Low Data Samples.

10. Choose Next.

11. Under Notification, choose In alarm and select an SNS topic to notify when the alarm is in ALARM state

To have the alarm send multiple notifications for the same alarm state or for different alarm states, choose Add notification.

To have the alarm not send notifications, choose Remove.

12. When finished, choose Next.

13. Enter a name and description for the alarm. The name must contain only ASCII characters. Then choose Next.

14. Under Preview and create, confirm that the information and conditions are what you want, then choose Create alarm.
