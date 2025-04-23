import tkinter as tk
from tkinter import ttk
import random
import time

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title('DSA Visualizer Tool')
        self.root.geometry('800x500')

        self.algorithms = ['Bubble Sort', 'Merge Sort', 'Quick Sort']
        self.selected_algorithm = tk.StringVar()
        self.speed = tk.DoubleVar()
        self.array_size = tk.IntVar()

        self.speed.set(0.1)
        self.array_size.set(50)

        self.data = []

        self.create_ui()

    def create_ui(self):
        control_frame = tk.Frame(self.root, padx=10, pady=10)
        control_frame.pack(fill=tk.X)

        tk.Label(control_frame, text='Algorithm:').grid(row=0, column=0, padx=5)
        algo_menu = ttk.Combobox(control_frame, textvariable=self.selected_algorithm, values=self.algorithms)
        algo_menu.grid(row=0, column=1, padx=5)
        algo_menu.current(0)

        tk.Label(control_frame, text='Speed:').grid(row=0, column=2, padx=5)
        speed_slider = tk.Scale(control_frame, variable=self.speed, from_=0.01, to=1.0, resolution=0.01, orient=tk.HORIZONTAL)
        speed_slider.grid(row=0, column=3, padx=5)

        tk.Label(control_frame, text='Size:').grid(row=0, column=4, padx=5)
        size_slider = tk.Scale(control_frame, variable=self.array_size, from_=10, to=100, orient=tk.HORIZONTAL)
        size_slider.grid(row=0, column=5, padx=5)

        tk.Button(control_frame, text='Generate', command=self.generate_array).grid(row=0, column=6, padx=5)
        tk.Button(control_frame, text='Start', command=self.start_sorting).grid(row=0, column=7, padx=5)

        self.canvas = tk.Canvas(self.root, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def generate_array(self):
        self.data = [random.randint(1, 100) for _ in range(self.array_size.get())]
        self.draw_data(self.data, ['blue' for _ in self.data])

    def draw_data(self, data, color_array):
        self.canvas.delete('all')
        c_height = 400
        c_width = 800
        x_width = c_width / (len(data) + 1)
        offset = 5
        spacing = 5
        normalized_data = [i / max(data) for i in data]

        for i, height in enumerate(normalized_data):
            x0 = i * x_width + offset + spacing
            y0 = c_height - height * 350
            x1 = (i + 1) * x_width + offset
            y1 = c_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        self.root.update_idletasks()

    def start_sorting(self):
        algo = self.selected_algorithm.get()
        if algo == 'Bubble Sort':
            self.bubble_sort()
        elif algo == 'Merge Sort':
            self.merge_sort(self.data)
        elif algo == 'Quick Sort':
            self.quick_sort(0, len(self.data)-1)
            self.draw_data(self.data, ['green' for _ in self.data])

    def bubble_sort(self):
        for i in range(len(self.data)):
            for j in range(0, len(self.data) - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                self.draw_data(self.data, ['green' if x == j or x == j+1 else 'blue' for x in range(len(self.data))])
                time.sleep(self.speed.get())

    def merge_sort(self, data):
        self._merge_sort(data, 0, len(data)-1)

    def _merge_sort(self, data, left, right):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort(data, left, mid)
            self._merge_sort(data, mid + 1, right)
            self._merge(data, left, mid, right)
            self.draw_data(data, ['green' if x >= left and x <= right else 'blue' for x in range(len(data))])
            time.sleep(self.speed.get())

    def _merge(self, data, left, mid, right):
        left_part = data[left:mid+1]
        right_part = data[mid+1:right+1]
        i = j = 0
        k = left
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                data[k] = left_part[i]
                i += 1
            else:
                data[k] = right_part[j]
                j += 1
            k += 1
        while i < len(left_part):
            data[k] = left_part[i]
            i += 1
            k += 1
        while j < len(right_part):
            data[k] = right_part[j]
            j += 1
            k += 1

    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi-1)
            self.quick_sort(pi+1, high)

    def partition(self, low, high):
        pivot = self.data[high]
        i = low - 1
        for j in range(low, high):
            if self.data[j] < pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
            self.draw_data(self.data, ['yellow' if x == j else 'red' if x == high else 'blue' for x in range(len(self.data))])
            time.sleep(self.speed.get())
        self.data[i+1], self.data[high] = self.data[high], self.data[i+1]
        return i + 1

if __name__ == '__main__':
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
