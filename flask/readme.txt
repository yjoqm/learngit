i简单来说，Blueprint 是一个存储操作方法的容器，这些操作在这个Blueprint 被注册到一个应用之后就可以被调用与招待，Flask 可以通过Blueprint来组织URL以及处理请求
但是如果你希望所有的 Blueprint 的请求都基于某一个固定的URL之后，刚我们可以在注册的时候指定其根路径的URL，比如我们想使用 http://127.0.0.1:5000/sample 这个地址来访问 sample 这个 Blueprint，刚可以使用下面这样的注册方法：

app.register_blueprint(sample,url_prefix='/sample')
