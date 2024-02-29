import matplotlib.pyplot as plt
from sklearn import datasets, model_selection, neural_network, metrics
from sklearn.metrics import confusion_matrix

# Load the Olivetti Faces dataset
olivetti_faces = datasets.fetch_olivetti_faces()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = model_selection.train_test_split(olivetti_faces.data, olivetti_faces.target, test_size=0.2, random_state=42)

# Train an MLP classifier
mlp = neural_network.MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
mlp.fit(X_train, y_train)

# Display ten entries from the testing data along with their true labels and predictions
predictions = mlp.predict(X_test[:10])
fig, axes = plt.subplots(2, 5, figsize=(12, 6))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_test[i].reshape(64, 64), cmap='gray')
    ax.set_title(f"True: {y_test[i]}, Predicted: {predictions[i]}")
    ax.axis('off')
plt.tight_layout()
plt.show()

# Calculate the confusion matrix for the testing data
conf_matrix = confusion_matrix(y_test, mlp.predict(X_test))

# Display the confusion matrix
plt.figure(figsize=(8, 6))
plt.imshow(conf_matrix, cmap='viridis')
plt.colorbar()
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()
