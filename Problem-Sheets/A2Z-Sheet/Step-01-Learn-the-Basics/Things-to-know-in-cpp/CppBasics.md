## C++ Basics

### Basic Structure / Syntax of C++
- In C++, the basic structure of a program consists of a main function, which serves as the entry point for the program. The main function is defined using the `int main()` syntax, and it typically returns an integer value to indicate the success or failure of the program.

```cpp
#include<iostream>
int main() {
    Code Here
    return 0;
}
 ```

---

### Output in C++
- To print something on the console, we use the `cout` object from the `iostream` library. The `<<` operator is used to send data to the output stream. std::cout is used to specify that we are using the cout object from the standard namespace.

```cpp
#include<iostream>
int main() {
    std::cout<<"Hey, Max!";
    return 0;
}
```

---

### Printing on the same line
- By default, `cout` does not add a newline after printing, so if you use multiple `cout` statements, they will print on the same line unless you explicitly add a newline character.

```cpp
#include<iostream>
int main() {
    std::cout << "Hey, Max!"; 
    std::cout << "Hello, World!"; 
}
```

---

### Printing on different lines
- To print on different lines, we can use the newline character `\n` or the `endl` manipulator. The `\n` character is an escape sequence that represents a newline, while `endl` is a manipulator that also inserts a newline and flushes the output buffer

```cpp
#include<iostream>
int main() {
    // We can use '\n' - endline escape sequence
    std::cout<< "Hey, Max!" << "\n";
    std::cout<< "Hey, Max!";
    // OR
    // We can alternatively use 'endl', which stands for endline
    std::cout<< "Hey, John!" << std::endl;
    std::cout<< "Hey, John!";
    return 0;
}
```

---

### Using namespace std
- The `std` namespace contains all the standard C++ library functions and objects.

- To avoid having to prefix every standard library function or object with `std::`, we can use the `using namespace std;` directive. This allows us to use the standard library functions and objects without the `std::` prefix.


```cpp
#include<iostream>
using namespace std;
int main() {
    cout << "Hey, Max!";
    return 0;
}
```

---

### Taking Input from user
- To take input from the user, we use the `cin` object from the `iostream` library. The `>>` operator is used to extract data from the input stream and store it in a variable.


```cpp
#include<iostream>
using namespace std;
int main() {
    int x;
    cin >> x;
    cout << "Value of x: " << x;
    return 0;
}
```

- For taking multiple inputs from the user, we can chain the `>>` operator to read multiple values in a single line.

```cpp
#include<iostream>
using namespace std;
int main() {
    int x, y;
    cin >> x >> y;
    cout << "Value of x:" << x << " and y:" << y;
    return 0;
}
```

---

### Using bits/stdc++.h
- The `bits/stdc++.h` header is a non-standard header file that includes all the standard C++ libraries. It is commonly used in competitive programming to save time and avoid including individual headers for each library.

- However, it is not recommended for use in production code or general programming, as it can lead to longer compilation times and may include unnecessary libraries that are not needed for the specific program. It is best to include only the necessary headers for your program to improve efficiency and readability.


So, we will use `bits/stdc++.h` in competitive programming for convenience, but in general programming, we should include only the specific headers we need.

```cpp
#include<bits/stdc++.h>
```

But if we want to include only the necessary headers, we can do it like this:

```cpp
#include<iostream>
#include<math.h>
```

Finally, here is an example of a complete C++ program that takes input from the user and prints it on the console using `bits/stdc++.h`:

```cpp
#include<bits/stdc++.h>
using namespace std;
int main() {
    int x, y;
    cin >> x >> y;
    cout << "Value of x:" << x << " and y:" << y;
    return 0;
}
```

---

### Arrays in C++
- An array is a collection of elements of the same type stored in contiguous memory locations. In C++, we can declare an array using the following syntax:
```cpp
type arrayName[arraySize];
```
- For example, to declare an array of integers with a size of 5, we can do it like this:
```cpp
int arr[5];
```
- We can also initialize an array at the time of declaration:
```cpp
int arr[5] = {1, 2, 3, 4, 5};
```
- We can access the elements of an array using their index, which starts from 0. For example, to access the first element of the array, we can use `arr[0]
```cpp
#include<iostream>
using namespace std;
int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    cout << "First element: " << arr[0] << endl; // Output: 1
    cout << "Second element: " << arr[1] << endl; // Output: 2
    cout << "Third element: " << arr[2] << endl; // Output: 3
    cout << "Fourth element: " << arr[3] << endl; // Output: 4
    cout << "Fifth element: " << arr[4] << endl; // Output: 5
}
```
- Arrays are zero-indexed, which means that the first element of the array is accessed using index 0, the second element using index 1, and so on. The last element of the array can be accessed using index `arraySize - 1`. In the above example, the last element can be accessed using `arr[4]` since the size of the array is 5.

- For Multidimensional arrays, we can declare them using the following syntax:
```cpp
type arrayName[size1][size2]...[sizeN];
```
- For example, to declare a 2D array of integers with 3 rows and 4 columns, we can do it like this:
```cpp
int arr[3][4];
```
- We can also initialize a 2D array at the time of declaration:
```cpp
int arr[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};
```
- We can access the elements of a 2D array using their row and column indices. For example, to access the element in the second row and third column, we can use `arr[1][2]` (since the indices start from 0):
```cpp
#include<iostream>
using namespace std;
int main() {
    int arr[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
};

    cout << "Element at second row and third column: " << arr[1][2] << endl; // Output: 7
    return 0;
}
```

This is how we can declare, initialize, and access elements of arrays in C++. Arrays are a fundamental data structure in C++ and are widely used for storing and manipulating collections of data.

---

Conditonals in C++
- Conditional statements in C++ allow us to execute different blocks of code based on certain conditions. The most common conditional statements in C++ are `if`, `else if`, and `else`.

##### TODO: Add examples for conditionals in C++.

