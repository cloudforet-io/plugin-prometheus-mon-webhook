# plugin-prometheus-monitoring-webhook
webhook for prometheus

# Data Model

## Prometheus Raw Data

Prometheus Notification Template Data Structure Reference : https://prometheus.io/docs/alerting/latest/notifications/#data
~~~
{
    'status': 'firing',
    'version': '4',
    'receiver': 'prometheus-spaceone-prometheus-webhook-alert-manager-config-spaceone-prometheus-webhook',
    'alerts': [
        {
            'generatorURL': 'http://prometheus-1-kube-promethe-prometheus.default:xxx,
            'status': 'firing',
            'annotations': {
                'description': 'Pod prometheus/prometheus-prometheus-node-exporter-xp6jv has been in a non-ready state for longer than 15 minutes.',
                'summary': 'Pod has been in a non-ready state for more than 15 minutes.',
                'runbook_url': 'https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.'
            },
            'fingerprint': '469fd6fbb9dbabaa',
            'labels': {
                'prometheus': 'default/prometheus-1-kube-promethe-prometheus',
                'severity': 'warning',
                'namespace': 'prometheus',
                'pod': 'prometheus-prometheus-node-exporter-xp6jv',
                'alertname': 'KubePodNotReady'
            },
            'startsAt': '2021-10-12T04:13:01.794Z',
            'endsAt': '0001-01-01T00:00:00Z'
        }
    ],
    'groupLabels': {},
    'truncatedAlerts': 0.0,
    'groupKey': '{}/{namespace="prometheus"}:{}',
    'commonLabels': {
        'pod': 'prometheus-prometheus-node-exporter-xp6jv',
        'namespace': 'prometheus',
        'prometheus': 'default/prometheus-1-kube-promethe-prometheus',
        'severity': 'warning',
        'alertname': 'KubePodNotReady'
    },
    'externalURL': 'http://prometheus-1-kube-promethe-alertmanager.default:9093',
    'commonAnnotations': {
        'description': 'Pod prometheus/prometheus-prometheus-node-exporter-xp6jv has been in a non-ready state for longer than 15 minutes.',
        'runbook_url': 'https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook#md#alert-name-kubepodnotready',
        'summary': 'Pod has been in a non-ready state for more than 15 minutes.'
    }
}
~~~
## SpaceONE Event Model

| Field		| Type | Description	| Example	|
| ---      | ---     | ---           | ---           |
| event_id | str  | auto generation | event-1234556  |
| event_key | str | fingerprint | 469fd6fbb9dbabaa |
| event_type | str | RECOVERY , ALERT based on `raw_data.state` | RECOVERY	|
| title | str	| `raw_data.annotations.summary`	| Pod has been in a non-ready state for more than 15 minutes.	|
| description | str | `raw_data.annotations.description`	| Pod prometheus/prometheus-xxx has been in a non-ready state for longer than 15 minutes.|
| severity | str  | alert level based `raw_data.alert.labels.severity (critical : CRITICAL / error : ERROR / warning: WARNING / info: INFO ` | ERROR |
| resource | dict | resource which triggered this alert	| ` {'pod':'prometheus-prometheus-node-exporter-xp6jv','alertname': 'KubePodNotReady'}` |
| raw_data | dict | Prometheus webhook received  data structure | - |
| additional_info | dict | `raw_data.alert.annotations` / `raw_data.alert.generatorURL`, `raw_data.alert.endsAt` | `{"org_id": "1.0", "rule_url" "https://...." }` |
| occured_at | datetime | prometheus alert triggered time , `alert.startsAt` | `2021-10-12T04:13:01.794Z`|
| alert_id | str | mapped alert_id	| alert-3243434343 |
| webhook_id | str  | webhook_id	| webhook-34324234234234 |
| project_id | str	| project_id	| project-12312323232    |
| domain_id | str	| domain_id	| domain-12121212121	|
| created_at | datetime | webhook alert created time | "2021-08-23T06:47:32.753Z"	|


## cURL Requests examples
This topic provides examples of calls to the SpaceONE Prometheus monitoring webhook using cURL.

Here's a cURL command that works for getting the response from webhook, you can test the following on your local machine.
```
curl -X POST https://your_spaceone_monitoring_webhook_url -d '{}'
 
```

Followings are examples which works for testing your own webhook.

```
curl -X POST https://{your_spaceone_monitoring_grafana_webhook_url} -d '{
  {
        'version': '4',
        'alerts': [
            {
                'labels': {
                    'prometheus': 'default/prometheus-1-kube-promethe-prometheus',
                    'severity': 'warning',
                    'alertname': 'KubePodNotReady',
                    'namespace': 'prometheus',
                    'pod': 'prometheus-prometheus-node-exporter-xp6jv'
                },
                'endsAt': '0001-01-01T00:00:00Z',
                'annotations': {
                    'description': 'Pod prometheus/prometheus-prometheus-node-exporter-xp6jv has been in a non-ready state for longer than 15 minutes.',
                    'runbook_url': 'https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodnotready',
                    'summary': 'Pod has been in a non-ready state for more than 15 minutes.'
                },
                'status': 'firing',
                'generatorURL': 'http://prometheus-1-kube-promethe-prometheus.default:9090/graph?g0.expr=sum+by%28namespace%2C+pod%29+%28max+by%28namespace%2C+pod%29+%28kube_pod_status_phase%7Bjob%3D%22kube-state-metrics%22%2Cnamespace%3D~%22.%2A%22%2Cphase%3D~%22Pending%7CUnknown%22%7D%29+%2A+on%28namespace%2C+pod%29+group_left%28owner_kind%29+topk+by%28namespace%2C+pod%29+%281%2C+max+by%28namespace%2C+pod%2C+owner_kind%29+%28kube_pod_owner%7Bowner_kind%21%3D%22Job%22%7D%29%29%29+%3E+0&g0.tab=1',
                'startsAt': '2021-10-12T04:13:01.794Z',
                'fingerprint': '469fd6fbb9dbabaa'
            }
        ],
        'truncatedAlerts': 0.0,
        'receiver': 'prometheus-spaceone-prometheus-webhook-alert-manager-config-spaceone-prometheus-webhook',
        'groupKey': '{}/{namespace="prometheus"}:{}',
        'status': 'firing',
        'commonAnnotations': {
            'description': 'Pod prometheus/prometheus-prometheus-node-exporter-xp6jv has been in a non-ready state for longer than 15 minutes.',
            'runbook_url': 'https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook.md#alert-name-kubepodnotready',
            'summary': 'Pod has been in a non-ready state for more than 15 minutes.'
        },
        'groupLabels': {},
        'commonLabels': {
            'severity': 'warning',
            'alertname': 'KubePodNotReady',
            'pod': 'prometheus-prometheus-node-exporter-xp6jv',
            'prometheus': 'default/prometheus-1-kube-promethe-prometheus',
            'namespace': 'prometheus'
        },
        'externalURL': 'http://prometheus-1-kube-promethe-alertmanager.default:9093'
    }
}'
```