from fastapi import FastAPI
import earthaccess
import pathlib

app = FastAPI()

@app.get("/")
async def read_root(short_name: str = None, 
                    start_date: str = "2024-05-01", 
                    end_date: str = "2024-05-16"
                    ):
    tspan = (start_date, end_date)
    bbox = (-76.75, 36.97, -75.74, 39.01)
    clouds = (0, 50)
    auth = earthaccess.login(strategy="environment")
    # results = earthaccess.search_datasets(instrument="oci") #Ocean Color Index = Sensor

    results = earthaccess.search_data(
      short_name="PACE_OCI_L2_BGC_NRT",
      temporal=tspan,
      bounding_box=bbox,
      cloud_cover=clouds,
    )   
    print("results", len(results))
    links = []
    for index in range(0, len(results)):
      links.append(results[index])

    return {"details" : links}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
