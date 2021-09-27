import logging
import unittest
import os
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.tester import TestCase, print_json

_LOGGER = logging.getLogger(__name__)
TEST_JSON = os.environ.get('test_json', None)


class TestEvent(TestCase):

    def test_parse(self):
        params1 = {
            "options": {

            },
            "data": {
                "groupLabels": {
                    "job": "prometheus-kube-prometheus-prometheus"
                },
                "alerts": [
                    {
                        "status": "firing",
                        "labels": {
                            "instance": "172.16.17.80:9090",
                            "container": "prometheus",
                            "job": "prometheus-kube-prometheus-prometheus",
                            "service": "prometheus-kube-prometheus-prometheus",
                            "endpoint": "web",
                            "prometheus": "prometheus/prometheus-kube-prometheus-prometheus",
                            "pod": "prometheus-prometheus-kube-prometheus-prometheus-0",
                            "namespace": "prometheus",
                            "rule_group": "/etc/prometheus/rules/prometheus-prometheus-kube-prometheus-prometheus-rulefil" +
                                          "es-0/prometheus-prometheus-kube-prometheus-kubelet.rules.yaml;kubelet.rules",
                            "severity": "critical",
                            "alertname": "PrometheusRuleFailures"
                        },
                        "annotations": {
                            "description": "Prometheus prometheus/prometheus-prometheus-kube-prometheus-prometheus-0 has f" +
                                           "ailed to evaluate 30 rules in the last 5m.",
                            "runbook_url": "https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook." +
                                           "md#alert-name-prometheusrulefailures",
                            "summary": "Prometheus is failing rule evaluations."
                        },
                        "fingerprint": "e2a3b36a4e1832ef",
                        "generatorURL": "http://prometheus-kube-prometheus-prometheus.prometheus:9090/graph?g0.expr=inc" +
                                        "rease%28prometheus_rule_evaluation_failures_total%7Bjob%3D%22prometheus-kube-p" +
                                        "rometheus-prometheus%22%2Cnamespace%3D%22prometheus%22%7D%5B5m%5D%29+%3E+0&g0." +
                                        "tab=1",
                        "endsAt": "0001-01-01T00:00:00Z",
                        "startsAt": "2021-08-23T05:16:56.154Z"
                    }, {
                        "generatorURL": "http://prometheus-kube-prometheus-prometheus.prometheus:9090/graph?g0.expr=inc" +
                                        "rease%28prometheus_rule_evaluation_failures_total%7Bjob%3D%22prometheus-kube-p" +
                                        "rometheus-prometheus%22%2Cnamespace%3D%22prometheus%22%7D%5B5m%5D%29+%3E+0&g0." +
                                        "tab=1",
                        "status": "firing",
                        "endsAt": "0001-01-01T00:00:00Z",
                        "annotations": {
                            "runbook_url": "https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook." +
                                           "md#alert-name-prometheusrulefailures",
                            "summary": "Prometheus is failing rule evaluations.",
                            "description": "Prometheus prometheus/prometheus-prometheus-kube-prometheus-prometheus-0 has f" +
                                           "ailed to evaluate 10 rules in the last 5m."
                        },
                        "labels": {
                            "endpoint": "web",
                            "alertname": "PrometheusRuleFailures",
                            "prometheus": "prometheus/prometheus-kube-prometheus-prometheus",
                            "container": "prometheus",
                            "severity": "critical",
                            "namespace": "prometheus",
                            "instance": "172.16.17.80:9090",
                            "job": "prometheus-kube-prometheus-prometheus",
                            "pod": "prometheus-prometheus-kube-prometheus-prometheus-0",
                            "service": "prometheus-kube-prometheus-prometheus",
                            "rule_group": "/etc/prometheus/rules/prometheus-prometheus-kube-prometheus-prometheus-rulefil" +
                                          "es-0/prometheus-prometheus-kube-prometheus-kubernetes-system-kubelet.yaml;kube" +
                                          "rnetes-system-kubelet"
                        },
                        "startsAt": "2021-08-23T05:16:56.154Z",
                        "fingerprint": "b81c57e53f0bff63"
                    }
                ],
                "groupKey": "{}/{namespace=\"prometheus\"}:{job=\"prometheus-kube-prometheus-prometheus\"}",
                "truncatedAlerts": 0.0,
                "commonLabels": {
                    "service": "prometheus-kube-prometheus-prometheus",
                    "alertname": "PrometheusRuleFailures",
                    "pod": "prometheus-prometheus-kube-prometheus-prometheus-0",
                    "instance": "172.16.17.80:9090",
                    "namespace": "prometheus",
                    "severity": "critical",
                    "prometheus": "prometheus/prometheus-kube-prometheus-prometheus",
                    "container": "prometheus",
                    "endpoint": "web",
                    "job": "prometheus-kube-prometheus-prometheus"
                },
                "status": "firing",
                "commonAnnotations": {
                    "summary": "Prometheus is failing rule evaluations.",
                    "runbook_url": "https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook." +
                                   "md#alert-name-prometheusrulefailures"
                },
                "version": "4",
                "receiver": "prometheus-spaceone-prometheus-webhook-alert-manager-config-spaceone-prometheu" +
                            "s-webhook",
                "externalURL": "http://prometheus-kube-prometheus-alertmanager.prometheus:9093"
            }

        }
        params2 = {
            "options": {},
            "data":{
                "externalURL": "http://prometheus-kube-prometheus-alertmanager.prometheus:9093",
                "commonAnnotations": {
                    "summary": "Prometheus is failing rule evaluations.",
                    "runbook_url": "https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook." +
                                   "md#alert-name-prometheusrulefailures"
                },
                "version": "4",
                "status": "firing",
                "groupLabels": {
                    "job": "prometheus-kube-prometheus-prometheus"
                },
                "commonLabels": {
                    "pod": "prometheus-prometheus-kube-prometheus-prometheus-0",
                    "prometheus": "prometheus/prometheus-kube-prometheus-prometheus",
                    "job": "prometheus-kube-prometheus-prometheus",
                    "severity": "critical",
                    "service": "prometheus-kube-prometheus-prometheus",
                    "container": "prometheus",
                    "endpoint": "web",
                    "instance": "172.16.17.80:9090",
                    "alertname": "PrometheusRuleFailures",
                    "namespace": "prometheus"
                },
                "alerts": [
                    {
                        "startsAt": "2021-08-23T05:16:56.154Z",
                        "annotations": {
                            "runbook_url": "https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook." +
                                           "md#alert-name-prometheusrulefailures",
                            "description": "Prometheus prometheus/prometheus-prometheus-kube-prometheus-prometheus-0 has f" +
                                           "ailed to evaluate 30 rules in the last 5m.",
                            "summary": "Prometheus is failing rule evaluations."
                        },
                        "endsAt": "0001-01-01T00:00:00Z",
                        "labels": {
                            "prometheus": "prometheus/prometheus-kube-prometheus-prometheus",
                            "severity": "critical",
                            "pod": "prometheus-prometheus-kube-prometheus-prometheus-0",
                            "endpoint": "web",
                            "job": "prometheus-kube-prometheus-prometheus",
                            "instance": "172.16.17.80:9090",
                            "alertname": "PrometheusRuleFailures",
                            "namespace": "prometheus",
                            "container": "prometheus",
                            "service": "prometheus-kube-prometheus-prometheus",
                            "rule_group": "/etc/prometheus/rules/prometheus-prometheus-kube-prometheus-prometheus-rulefil" +
                                          "es-0/prometheus-prometheus-kube-prometheus-kubelet.rules.yaml;kubelet.rules"
                        },
                        "status": "firing",
                        "fingerprint": "e2a3b36a4e1832ef",
                        "generatorURL": "http://prometheus-kube-prometheus-prometheus.prometheus:9090/graph?g0.expr=inc" +
                                        "rease%28prometheus_rule_evaluation_failures_total%7Bjob%3D%22prometheus-kube-p" +
                                        "rometheus-prometheus%22%2Cnamespace%3D%22prometheus%22%7D%5B5m%5D%29+%3E+0&g0." +
                                        "tab=1"
                    }, {
                        "generatorURL": "http://prometheus-kube-prometheus-prometheus.prometheus:9090/graph?g0.expr=inc" +
                                        "rease%28prometheus_rule_evaluation_failures_total%7Bjob%3D%22prometheus-kube-p" +
                                        "rometheus-prometheus%22%2Cnamespace%3D%22prometheus%22%7D%5B5m%5D%29+%3E+0&g0." +
                                        "tab=1",
                        "status": "firing",
                        "labels": {
                            "endpoint": "web",
                            "pod": "prometheus-prometheus-kube-prometheus-prometheus-0",
                            "namespace": "prometheus",
                            "service": "prometheus-kube-prometheus-prometheus",
                            "severity": "critical",
                            "instance": "172.16.17.80:9090",
                            "job": "prometheus-kube-prometheus-prometheus",
                            "container": "prometheus",
                            "prometheus": "prometheus/prometheus-kube-prometheus-prometheus",
                            "alertname": "PrometheusRuleFailures",
                            "rule_group": "/etc/prometheus/rules/prometheus-prometheus-kube-prometheus-prometheus-rulefil" +
                                          "es-0/prometheus-prometheus-kube-prometheus-kubernetes-system-kubelet.yaml;kube" +
                                          "rnetes-system-kubelet"
                        },
                        "endsAt": "0001-01-01T00:00:00Z",
                        "fingerprint": "b81c57e53f0bff63",
                        "annotations": {
                            "summary": "Prometheus is failing rule evaluations.",
                            "description": "Prometheus prometheus/prometheus-prometheus-kube-prometheus-prometheus-0 has f" +
                                           "ailed to evaluate 10 rules in the last 5m.",
                            "runbook_url": "https://github.com/kubernetes-monitoring/kubernetes-mixin/tree/master/runbook." +
                                           "md#alert-name-prometheusrulefailures"
                        },
                        "startsAt": "2021-08-23T05:16:56.154Z"
                    }
                ],
                "receiver": "prometheus-spaceone-prometheus-webhook-alert-manager-config-spaceone-prometheu" +
                            "s-webhook",
                "truncatedAlerts": 0.0,
                "groupKey": "{}/{namespace=\"prometheus\"}:{job=\"prometheus-kube-prometheus-prometheus\"}"
            }
        }
        #params1, params2, params3, params4,
        test_cases = [params1, params2]

        for idx, test_case in enumerate(test_cases):
            print(f'###### {idx} ########')
            data = test_case.get('data')
            parsed_data = self.monitoring.Event.parse({'options': {}, 'data': data})
            print(parsed_data)



if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
