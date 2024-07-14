from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


def create_scaler(data, scaler_type="standard"):
    scaler_map = {
        "standard": StandardScaler,
        "std": StandardScaler,
        "minmax": MinMaxScaler,
        "mm": MinMaxScaler,
    }

    if not scaler_type in scaler_map:
        raise Exception("Invalid scaler type")

    scaler = scaler_map[scaler_type]()
    scaler.fit(data)

    def scaler_wrapper(data):
        return scaler.transform(data)

    return scaler_wrapper
