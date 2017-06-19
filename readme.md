# django 权限设计

### 初步设计完成,集成到django权限设计当中，不过感觉还是不太合理应该有改进的空间

## 核心 
` permission这个装饰器里面, `,` 以及models权限表的设计, `
注意 permission这个表的后面
```
permissions = (
            ('views_student_list', '查看学员信息表'),
            ('views_student_info', '查看学员详细信息'),
            ('home', '登录首页')
        )
```
这个是一定要加的， 加上之后可以在django后台随意控制权限了


