---

# **Object Localization Network**

This repository contains Python scripts for **class-agnostic object localization** using the **Object Localization Network (OLN)** model in **ONNX format**. The model is designed to detect and localize objects in images or videos without requiring class-specific information, making it highly versatile for various applications.

![Object-Localization-Network Video](https://github.com/Gaurav14cs17/Object-Localization-Network/blob/main/doc/img/video.gif)

---

## **Features**
- **Class-Agnostic Object Localization**: Detects and localizes objects without requiring class labels.
- **ONNX Model**: The model is provided in ONNX format for easy deployment and inference.
- **Real-Time Performance**: Optimized for real-time object localization tasks.
- **Cross-Platform Compatibility**: Works seamlessly across different platforms and frameworks.

---

## **Getting Started**

### **1. Download the ONNX Weight File**
- Download the ONNX weight file from [here](https://www.dropbox.com/s/ztrp5liphjee623/oln_720x1280.onnx?dl=0).
- Place the downloaded file (`oln_720x1280.onnx`) in the `onnx_weight` folder.

### **2. Install Dependencies**
Ensure you have the required dependencies installed. You can install them using `pip`:

```bash
pip install onnxruntime opencv-python numpy
```

### **3. Run the Script**
Use the provided Python scripts to perform object localization on images or videos. For example:

```bash
python object_localization.py --input input_image.jpg --output output_image.jpg
```

---

## **Model Details**

### **Object Localization Network (OLN)**
The **Object Localization Network (OLN)** is a class-agnostic object detection model that focuses on **localizing objects** without requiring class-specific information. It is particularly useful for tasks where the goal is to detect objects regardless of their categories.

#### **Key Features of OLN**
- **Class-Agnostic**: Detects objects without relying on predefined classes.
- **High Accuracy**: Achieves state-of-the-art performance in object localization tasks.
- **Efficient**: Optimized for real-time performance.

### **ONNX Model**
The model is provided in **ONNX (Open Neural Network Exchange)** format, which allows for **cross-platform compatibility** and easy integration with various frameworks like TensorFlow, PyTorch, and ONNX Runtime.

---

## **Results**

### **Video Demo**
Check out the video demo of the Object Localization Network in action:

![Object-Localization-Network Video](https://github.com/Gaurav14cs17/Object-Localization-Network/blob/main/doc/img/video.gif)

---

## **References**

### **Model and Code**
- **Object-Localization-Network Model**: [GitHub Repository](https://github.com/mcahny/object_localization_network)
- **PINTO0309's Model Zoo**: [GitHub Repository](https://github.com/PINTO0309/PINTO_model_zoo)

### **Research Paper**
- **Original Paper**: [OLN: Object Localization Network](https://arxiv.org/abs/2108.06753)

### **ONNX Implementation**
- **ONNX Model**: [GitHub Repository](https://github.com/ibaiGorordo/ONNX-Object-Localization-Network)

---

## **Folder Structure**
Here’s an overview of the repository structure:

```
Object-Localization-Network/
├── onnx_weight/              # Folder to store the ONNX weight file
│   └── oln_720x1280.onnx     # ONNX weight file
├── scripts/                  # Python scripts for inference
│   └── object_localization.py
├── doc/                      # Documentation and resources
│   └── img/                  # Images and GIFs
│       └── video.gif         # Demo video
└── README.md                 # Project README file
```

---

## **How to Contribute**
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Submit a pull request.

---

## **License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
- Thanks to the authors of the **Object Localization Network** for their research and model.
- Special thanks to **PINTO0309** for maintaining the model zoo and providing ONNX models.
- Thanks to the **ONNX community** for their support and tools.

---
