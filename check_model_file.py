import os


def check_model_file(file_path):
    if os.path.exists(file_path):
        print(f"Model file found at: {file_path}")
    else:
        print(f"Model file not found at: {file_path}")


if __name__ == "__main__":
    # Specify the path to your model file
    model_file_path = 'model/emotion_model.h5'

    # Check if the model file exists
    check_model_file(model_file_path)
