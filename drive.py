from util import api_covid

api_ref=api_covid.CovidAPI()
async def resp():
    print(await api_ref.get_all_data())
await resp()