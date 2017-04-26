# first time
./update-dynamic-hosts.sh

../virtualenv/bin/ansible-playbook deploy-sensu.yaml -l monitoring-server

pasword: r00tme
# update

../virtualenv/bin/ansible-playbook deploy-sensu.yaml -l monitoring-server

# gerrit review repo
git push origin HEAD:refs/for/master

### Add handler 
1. list handler in ansible.hosts.d/group_vars/sensu_masters.yaml
    the basename of the filename has to be specified. In my case, testudp-hander or kafka-handler
    handlers:
      - graphite-handler
      - mailer
      - mailer-handler
      - xmpp
      - xmpp-handler
      - kafka-handler
2. Add the handler to the check you want to monitor in  ansible.hosts.d/group_vars/monitored-hosts.yaml
    metrics:
        cpu_metrics:
            name: cpu-metrics
            command: metrics-cpu.rb --scheme "{{ metrics_scheme }}.cpu" | grep -vE 'cpu\.cpu[0-9]+\.'
            interval: 5
            handlers:
                - graphite
                - kafka
        network_metrics:
            ...

3. handler script (handler-kafka.rb) under roles/sensu/templates/check-plugin/
4. handler config file (kafka-handler.json.j2) in roles/sensu/templates/
    {
      "handlers": {
        "kafka": {
          "type": "pipe",
          "command": "handler-kafka.rb",
        }
      }
    }
5. add entry in host_vars/monitoring-server.yaml
    check_plugins: # note that check_plugins might be changed into "plugins"
        ...
        kafka: handler-kafka.rb
