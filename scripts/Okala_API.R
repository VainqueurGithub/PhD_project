install.packages("remotes")
install.packages("httr2", type = "binary")

library(remotes)
library(httr2)

install.packages("NatureCubeR", dependencies = TRUE)

library(NatureCubeR)

# API KEY

hdr <- auth_headers(get_key(api_key = "gmSX8UPThL1HvP5ErLqOpznHD9VOOK38sn5BHCE3ZvskVWHbfF1LkRwCy4G5LKhS5RyY6NVNCxyMD0YGM12qiAg02qHP1ylw8gym"))

get_project(hdr)

stations <- get_station_info(hdr = hdr, datatype = "image")
stations

psr_ids <- stations$project_system_record_id

media_assets <- get_media_assets(
  hdr      = hdr,
  datatype = "image",
  psrID    = psr_ids
)

media_assets
