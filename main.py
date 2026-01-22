from import_data.importer import Importer, import_weapons


if __name__ == "__main__":
    Importer("blip_models").import_data()
    Importer("blip_colors").import_data()
    Importer("markers").import_data()
    Importer("ped_models").import_data()
    import_weapons()
