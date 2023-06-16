
![Logo](https://www.kite.com/wp-content/uploads/2019/05/common-base-template-gif-django-2.gif)


# First [django] web project



##  Reference of project

#### Get all items

```http
  GET /framwork/items
```

| Parameter | Type     | Description                |
| :---- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /framwork/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

