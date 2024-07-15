# FastAPIRichLogger

## Description
FastAPIRichLogger is a robust and visually appealing logging system for FastAPI applications. Utilizing the power of the `rich` library, it enhances the standard logging capabilities with color-coded log levels, detailed request-response data, and a user-friendly format that improves both readability and debugging.

## Installation
Install FastAPIRichLogger with pip:

```bash
pip install fastapirichlogger
```

## Usage
To use FastAPIRichLogger in your FastAPI application, follow these steps:

1. **Import FastAPIRichLogger**:
   ```python
   from fastapirichlogger import FastAPIRichLogger
   ```

2. **Add Middleware to FastAPI**:
   ```python
   app = FastAPI()
   app.add_middleware(FastAPIRichLogger)
   ```

## Features
- **Color-Coded Logging**: Easily distinguish between different log levels thanks to color coding.
- **Request-Response Details**: Logs include detailed information about HTTP requests and responses.
- **Execution Time Tracking**: Monitor the time taken for each request to process.
- **Automatic Log ID Assignment**: Each request gets a unique log identifier for easier tracking.

## Example Images

Below are example images showing the FastAPIRichLogger in action:

- **Success Log Example**:
  ![Success Log](https://gcdnb.pbrd.co/images/CNZuN81Gf4Hn.png)

- **Error Log Example**:
  ![Error Log](https://gcdnb.pbrd.co/images/QfpPhSLCf1Xy.png)

## Contributing
Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE.md` for more information.

## Contact
Kevin Saltarelli - kevinqz@gmail.com

Project Link: [https://github.com/kevinqz/fastapirichlogger](https://github.com/kevinqz/fastapirichlogger)