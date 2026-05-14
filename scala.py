Here is a step-by-step guide to setting up Apache Spark on your Windows laptop and running a simple Scala program.

The easiest way to get started with Spark on Windows is to set up the necessary dependencies, install Spark, and then use its interactive shell (`spark-shell`) to run Scala code without needing a full IDE.

### Step 1: Install Java and Python

Spark requires Java, and its Scala shell also works best with Python. Since paths with spaces can cause issues, we will install them in a root folder like `C:\`.

1.  Open **Command Prompt** as an **Administrator**.
2.  Run the following commands to install Java and Python using the Windows Package Manager:
    ```bash
    winget install --id Azul.Zulu.21.JDK -e --source winget
    winget install --id Python.Python.3.9 -e --source winget
    ```

3.  Move the Java installation to a path without spaces:
    ```bash
    mkdir C:\Zulu
    robocopy "C:\Program Files\Zulu\zulu-21" "C:\Zulu\zulu-21" /E /MOVE
    ```

4.  Verify the installations:
    ```bash
    java -version
    python --version
    ```

### Step 2: Download and Install Apache Spark

1.  Go to the [Apache Spark downloads page](https://spark.apache.org/downloads.html). Select the latest Spark release (e.g., 3.5.3) and the package type "Pre-built for Apache Hadoop".
2.  Download the `.tgz` file (e.g., `spark-3.5.3-bin-hadoop3.tgz`).
3.  Extract the file to `C:\Spark`. You can use a tool like 7-Zip:
    ```bash
    mkdir C:\Spark
    "C:\Program Files\7-Zip\7z.exe" x "C:\Users\YourUsername\Downloads\spark-3.5.3-bin-hadoop3.tgz" -oC:\Spark
    "C:\Program Files\7-Zip\7z.exe" x "C:\Spark\spark-3.5.3-bin-hadoop3.tar" -oC:\Spark
    ```

### Step 3: Add `winutils.exe`

Spark needs `winutils.exe` to interact with the Windows file system correctly.

1.  Create a `hadoop\bin` folder in `C:\`:
    ```bash
    mkdir C:\hadoop\bin
    ```

2.  Download the `winutils.exe` file corresponding to your Hadoop version (e.g., for Hadoop 3.3):
    ```bash
    curl --ssl-no-revoke -L -o C:\hadoop\bin\winutils.exe https://github.com/cdarlint/winutils/raw/master/hadoop-3.3.5/bin/winutils.exe
    ```

### Step 4: Set Up Environment Variables

This step allows you to run Spark commands from any location in the Command Prompt.

Run the following commands in Command Prompt (as Administrator), adjusting paths if you used different versions:
```bash
setx SPARK_HOME "C:\Spark\spark-3.5.3-bin-hadoop3"
setx HADOOP_HOME "C:\hadoop"
setx JAVA_HOME "C:\Zulu\zulu-21"

:: Add to PATH
for /f "tokens=2*" %A in ('reg query "HKCU\Environment" /v Path') do set "oldPath=%B"
setx Path "%oldPath%;%SPARK_HOME%\bin;%HADOOP_HOME%\bin;%JAVA_HOME%\bin"
```
**Restart Command Prompt** for the changes to take effect.

### Step 5: Run Your First Scala Program with Spark

Now for the exciting part—running actual code. The `spark-shell` is an interactive tool that lets you write and run Scala code line by line, which is perfect for learning.

1.  In a new Command Prompt, type `spark-shell` and press Enter. This will launch the Scala shell. You will see a welcome message and a `scala>` prompt.
2.  You now have a `SparkContext` (an object named `sc`) available, which is the main entry point for Spark functionality.
3.  Let's start with a classic "Hello, World" example. Type this at the `scala>` prompt and press Enter:
    ```scala
    println("Hello, Apache Spark on Windows!")
    ```
4.  For a more practical example, let's analyze text. First, create a simple text file named `sample.txt` on your `C:\` drive with a few sentences.
5.  Now, run the following Scala code in the `spark-shell` to read the file and count word frequencies. This demonstrates Spark's powerful data processing capabilities:
    ```scala
    // Read the file into an RDD (Resilient Distributed Dataset)
    val textFile = sc.textFile("C:/sample.txt")
    
    // Split lines into words, count occurrences, and sort by count
    val wordCounts = textFile
        .flatMap(line => line.split(" "))
        .map(word => (word, 1))
        .reduceByKey(_ + _)
        .map(_.swap) // Swap to (count, word) for sorting
        .sortByKey(ascending = false)
    
    // Collect and print the results
    wordCounts.collect().foreach(println)
    ```
6.  To exit the `spark-shell`, type `:quit` or press `Ctrl + D`.

### Understanding the Sample Code

- `sc.textFile(...)`: This loads the text file from your local drive into a distributed dataset called an RDD.
- `.flatMap(_.split(" "))`: This goes through each line and splits it into individual words.
- `.map((_, 1))`: This transforms each word into a key-value pair, where the key is the word and the value is 1 (e.g., "spark" -> ("spark", 1)).
- `.reduceByKey(_ + _)`: This is the core of the word count. It finds all pairs with the same key (word) and adds their values together to get the total count.
- `.collect()`: This brings all the results from the Spark cluster (in your case, your single laptop) back to the driver program so you can print them.

This practical setup turns your Windows laptop into a development environment for big data processing, allowing you to learn and prototype Spark applications using Scala.
