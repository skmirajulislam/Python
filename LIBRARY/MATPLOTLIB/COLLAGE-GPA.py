import matplotlib.pyplot as plt

# Sample GPA data (replace this with your actual GPA data)
gpa_data = [7.9, 8.6, 9.7, 9.4, 8.9]

# Generate x-axis labels (assuming each data point represents a semester)
semesters = [f"Semester {i+1}" for i in range(len(gpa_data))]

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(semesters, gpa_data, color='skyblue')
plt.title('College GPA Over Semesters \n Sk Mirajul islam')
plt.xlabel('Semesters')
plt.ylabel('GPA')
plt.ylim(0, 10)  # Limit the y-axis from 0 to 4 (assuming GPA is on a 4.0 scale)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()

# Display the plot
plt.show()
