## Документация для запуска контейнера c backend-сервером  
1. **Сначала собрать образ командой**:  
    `docker build . -t <image_name>`
2. **Затем запустить контейнер командой** *(вместо 8000 порта можно указать какой угодно)*:  
    `docker run -d -p 8000:5555 --name <container_name> <image_name>`
3. **После этого можно отправлять `GET/POST` HTTP запросы на `localhost`, на следующие пути** *(с указанием нужного порта)*:  
    - `http://localhost:8000/api/v1/products`
    - `http://localhost:8000/api/v1/stocks`  
    **Либо `GET/PATCH/PUT/DELETE` на следующие**:  
    - `http://localhost:8000/api/v1/products/<pk>`
    - `http://localhost:8000/api/v1/stocks/<pk>`