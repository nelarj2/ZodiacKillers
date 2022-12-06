# Grafana
Start grafana
docker run --add-host=host.docker.internal:host-gateway -p 3000:3000 grafana/grafana-enterprise
Add http://docker.for.mac.localhost:9090 as datasource
Add dashboard.json

# Prom
Start Prom
docker run --add-host=host.docker.internal:host-gateway -v $(pwd)/prom.yml:/etc/prometheus/prometheus.yml  -p 9090:9090 prom/prometheus

# Run cli
pip install -r requirements.txt
python cli.py