"""
post请求：request.data
get请求：request.query_params
---------------------------------------------------------------------------------------------------------
__View__
VIEW: Django view 有dispatch(), as_view()
APIView: 继承View, 重写dispatch(): 1.构建新的request对象 2.初始化 认证，权限，限流
GenericAPIView: 继承APIView 提供四个内置方法
                serializer_class = xSerializer
                queryset = x.objects.all()
                增删改查查直接简化为
                1. 继承mixin
                2. post调用create, get调用list...
Mixin: 完成增删查改逻辑，create，list...
GenericAPIView搭配Mixin使用

ViewSetMixin：重塑分发机制 允许自己更改路由，比如 get->list, post->create
ViewSet: 继承ViewSetMixin和APIView，允许更改路由，允许合并两个view类(带id和不带id)

GenericViewSet：GenericAPIView + ViewSetMixin
ModelViewSet: 完成增删查改逻辑，集大成者 GenericViewSet + mixin
              只写两行
              serializer_class = xSerializer UI界面测试时基于哪个表单渲染
              queryset = x.objects.all()
              完成所有功能(create, list...)
目前的路由已经实现路由重新分发(get->list.....)
---------------------------------------------------------------------------------------------------------
__Serializer__
针对模型设计序列化器
serializers.Serializer: view里serializer.is_valid()方法构建两个变量
                        serializer.errors错误
                        serializer.validated_data成功校验的结果
                        view里serializer.save() 包含了update()/create()
                        但是要自己在serializer实现update()/create(), 传参时有instance时是update()
                        update()/create()会创建self.instance, 返回值是self.instance
                        serializer.data是serializer.instance的序列化结果
serializers.ModelSerializer: class Meta里的 model = x模型 就是针对模型x做序列化, 自动实现create()和update()
---------------------------------------------------------------------------------------------------------
utils:跨工程
service:当前app
"""
