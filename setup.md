# Prom
Start Prom

- For mac, run `docker run --add-host=host.docker.internal:host-gateway -v $(pwd)/prom_mac.yml:/etc/prometheus/prometheus.yml  -p 9090:9090 prom/prometheus`
- For windows, run `docker run --add-host=host.docker.internal:host-gateway -v $(pwd)/prom_win.yml:/etc/prometheus/prometheus.yml  -p 9090:9090 prom/prometheus`

# Grafana
Start grafana

- docker run --add-host=host.docker.internal:host-gateway -p 3000:3000 grafana/grafana-enterprise

- Go to localhost:3000 (login using user: admin password: admin)

- Skip password setup

- Add datasource
    - Hover over gear on the bottom of the left navigation bar
    - Click on "Data sources"
    - Click on "Add data source" button
    - Click on "Prometheus"
    - For mac, add http://docker.for.mac.localhost:9090 in the URL field
    - For windows, add http://host.docker.internal:9090 in the URL field 
    - Click on Save & test

- Add dashboard
    - Hover over Dashboards button on the left navbar (looks like four squares)
    - Click pn "+ Import"
    - Click on "Upload JSON File"
    - Select dashboard.json found in this repo
    - Click on "Select a Prometheus data source" dropdown menu
    - Select "Prometheus"
    - Click on "Import" button

# Run app

- pip install -r requirements.txt
- cd UI
- python app.py