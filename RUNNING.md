# Instructions for running the pipeline in Google Cloud

## Create instance
```bash
gcloud beta compute --project=open-targets-eu-dev instances create tskir-epmc --zone=europe-west1-d --machine-type=n1-standard-64 --subnet=default --network-tier=PREMIUM --maintenance-policy=MIGRATE --service-account=426265110888-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/cloud-platform --image=ubuntu-2004-focal-v20210908 --image-project=ubuntu-os-cloud --boot-disk-size=1000GB --boot-disk-type=pd-balanced --boot-disk-device-name=tskir-epmc --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any
```

## Start and connect to instance
```bash
gcloud compute instances start --zone "europe-west1-d" "tskir-epmc"  --project "open-targets-eu-dev"
gcloud beta compute ssh --zone "europe-west1-d" "tskir-epmc"  --project "open-targets-eu-dev"
```

### Prepare running environment
```bash
git clone https://github.com/tskir/epmc-ambiguity
cd epmc-ambiguity
sudo apt update
sudo apt install python3-pip openjdk-11-jdk
python3 -m pip install -r requirements.txt
```

### Download data
```bash
rm -rf matches
gsutil -m cp -r gs://open-targets-pre-data-releases/21.08.1/output/literature/parquet/matches .
```

### Update code, run, shut down
```bash
screen
git pull
rm -rf matches_filtered
time python3 prototype.py --matches matches --filtered-output matches_filtered > README.md
gsutil -m cp -r matches_filtered gs://ot-team/tskir/matches_filtered_2021-09-14
gsutil cp README.md gs://ot-team/tskir/matches_filtered_2021-09-14.README.md
sudo shutdown -h now
```
