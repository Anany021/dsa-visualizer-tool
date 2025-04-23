import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="DSA Visualizer Tool", layout="wide")

# Sorting Algorithms
def bubble_sort(data, speed, plot_area):
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            draw_plot(data, ["green" if x == j or x == j + 1 else "blue" for x in range(len(data))], plot_area)
            time.sleep(speed)

def merge_sort(data, l, r, speed, plot_area):
    if l < r:
        m = (l + r) // 2
        merge_sort(data, l, m, speed, plot_area)
        merge_sort(data, m + 1, r, speed, plot_area)
        merge(data, l, m, r, speed, plot_area)

def merge(data, l, m, r, speed, plot_area):
    left = data[l:m+1]
    right = data[m+1:r+1]

    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1
        draw_plot(data, ["green" if x >= l and x <= r else "blue" for x in range(len(data))], plot_area)
        time.sleep(speed)

    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1

def quick_sort(data, low, high, speed, plot_area):
    if low < high:
        pi = partition(data, low, high, speed, plot_area)
        quick_sort(data, low, pi - 1, speed, plot_area)
        quick_sort(data, pi + 1, high, speed, plot_area)

def partition(data, low, high, speed, plot_area):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
        draw_plot(data, ["yellow" if x == j else "red" if x == high else "blue" for x in range(len(data))], plot_area)
        time.sleep(speed)
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1

def draw_plot(data, color_array, plot_area):
    fig, ax = plt.subplots()
    ax.clear()
    sns.barplot(x=list(range(len(data))), y=data, palette=color_array, ax=ax)
    plot_area.pyplot(fig)

# UI Elements
st.title("DSA Visualizer Tool")

algo = st.selectbox("Choose Algorithm", ["Bubble Sort", "Merge Sort", "Quick Sort"])
speed = st.slider("Sorting Speed (seconds)", 0.01, 1.0, 0.1)
size = st.slider("Array Size", 5, 30, 15)

plot_area = st.empty()

if st.button("Generate Array"):
    st.session_state.data = np.random.randint(1, 100, size).tolist()
    draw_plot(st.session_state.data, ["blue" for _ in st.session_state.data], plot_area)

if "data" in st.session_state:
    if st.button("Start Sorting"):
        if algo == "Bubble Sort":
            bubble_sort(st.session_state.data, speed, plot_area)
        elif algo == "Merge Sort":
            merge_sort(st.session_state.data, 0, len(st.session_state.data) - 1, speed, plot_area)
            draw_plot(st.session_state.data, ["green" for _ in st.session_state.data], plot_area)
        elif algo == "Quick Sort":
            quick_sort(st.session_state.data, 0, len(st.session_state.data) - 1, speed, plot_area)
            draw_plot(st.session_state.data, ["green" for _ in st.session_state.data], plot_area)
