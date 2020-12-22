# Setup guide
1. Install docker (see their website. should be easy for windows)
2. Pull postgres image
  `docker pull postgres`
3. Run the image (update password below)
  `docker run -d --name=dusri-naukari-db -p 5432:5432 -e POSTGRES_PASSWORD=<some-password> postgres`
