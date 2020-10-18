## AWS Billing Alarm to Monitor Your AWS Bill

You can monitor your estimated AWS charges by using Amazon CloudWatch.

## Enabling Billing Alerts

1. Open the Billing and Cost Management console at https://console.aws.amazon.com/billing/.
2. In the navigation pane, choose Billing Preferences.
3. Choose Receive Billing Alerts.
4. Choose Save preferences.

## Creating a Billing Alarm

```
Before you can create a billing alarm,you must enable billing alerts in your account, or in the master/payer account if you are using consolidated billing.
```

1. Open the CloudWatch console at https://console.aws.amazon.com/cloudwatch/.

2. If necessary, change the Region to US East (N. Virginia). Billing metric data is stored in this Region and represents worldwide charges.

3. In the navigation pane, choose Alarms, Create Alarm.

4. Choose Select metric. In the All metrics tab, choose Billing, Total Estimated Charge.

If you don't see Billing or the Total Estimated Charge metric, you may need to enable billing alerts. For more information, see Enabling Billing Alerts.

5. Select the check box next to EstimatedCharges, and choose Select metric.

6. Under Conditions, choose Static.

7. For Whenever EstimatedCharges is, choose Greater.

8. For than, enter the monthly amount (for example, 200) that must be exceeded to trigger the alarm.

9. Choose Next.

10. For Select an SNS topic, select an SNS topic to notify when the alarm is in ALARM state, or create a new topic to be notified.

To have the alarm send multiple notifications for the same alarm state or for different alarm states, choose Add notification.

11. When finished, choose Next.

12. Enter a name and description for the alarm. The name must contain only ASCII characters. Then choose Next.

13. Under Preview and create, confirm that the information and conditions are what you want, then choose Create alarm.