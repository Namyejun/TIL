### 10. JDBC 실습 - ResultSet의 데이터를 POJO class로 매핑하기

자바는 객체지향 언어이다. 매번 코드로 SQL의 쿼리 결과의 몇 번째 값이 어떤 타입의 데이터이다는 것을 코드로 짜려면 **시간도 오래걸릴 뿐더러**, 작성자가 아닌 다른 사람이 **코드를 읽기도 불편하다**.

**ResultSet의 결과를 Java Object로 만들면** 타입 안정성과 객체지향 프로그래밍의 장점을 살려서 프로그램을 간결하게 만들 수 있다.

```java
package org.de.jdbc.mapper;

import java.time.LocalDateTime;

public class Product {
	int id;
	String name;
	LocalDateTime updated_at;
	String contents;
	int price;

	public Product(int id, String name, LocalDateTime updated_at, String contents, int price) {
		this.id = id;
		this.name = name;
		this.updated_at = updated_at;
		this.contents = contents;
		this.price = price;
	}

	@Override
	public String toString() {
		return "Product{" +
			"id=" + id +
			", name='" + name + '\'' +
			", updated_at=" + updated_at +
			", contents='" + contents + '\'' +
			", price=" + price +
		'}';
	}
}
```

```java
package org.de.jdbc.mapper;

import java.sql.ResultSet;
import java.sql.SQLException;

public class ResultSetMapper {
	public static Product create(ResultSet rs) throws SQLException {
		return new Product(rs.getInt(1), rs.getString(2),
			rs.getTimestamp(3).toLocalDateTime(), rs.getString(4),
			rs.getInt(5));
	}
}
```

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import org.de.jdbc.mappe.Product;
import org.de.jdbc.mappe.ResultSetMapper;

public class Main {
	public static void main(String[] args) throws SQLException {
		//here de-jdbc is database name, root is username and password is null. Fix them for your database settings.
		Connection con = DriverManager.getConnection(
			"jdbc:mysql://localhost:3306/de-jdbc", "root", null);
		Statement stmt = con.createStatement();
		ResultSet rs = stmt.executeQuery("select `id`, `name`, `updated_at`, `contents`, `price` from product");
		while (rs.next()) {
			System.out.println(ResultSetMapper.create(rs));
		}
		con.close();
	}
}
```

하지만 이런 방식은, 내가 수행하는 **SELECT문의 모든 결과를 별도의 Java Class로 선언**해놓아야 가능하다. 그리고 **데이터를 변환하는 함수도 SELECT문의 결과에 따라 각각 만들어놓아야 한다.** 실제로 업무에서 활용하려면 이런 코드를 짜는데 **시간이 굉장히 많이 들어간다**. 그리고 ResultSet은 index별로 타입을 구분해서 함수를 호출해야하므로 **쿼리나 코드의 변경에도 버그가 발생할 확률이 높아진다**. **즉, 변경에 취약하다.**

이런 ResultSet과 POJO class 를 **매핑하는 코드를 매번 짜는 것이 불편해서 만들어진 기술**(Library)을 `ORM(Object-Relational Mapping)`이다. 이름에서 추론할 수 있는 바와 같이, **객체와 Relational Model(관계형 데이터베이스 모델)을 매핑할 수 있는 기능**을 가지고 있다. **하나의 테이블이 하나의 Java Class에 해당**하고, **FK와 같은 부가적인 기능은 함수로 제공**한다.
ORM에 대해서는 6에서 더 다룬다.

### 11. JDBC 실습 - PreparedStatement

**Statement를 상속받는다**. **parameterized query를 사용**할 때 쓴다. **변수를 사용**할 수 있어서 Statement 종류 중에 가장 활용도가 높다.

여러 종류의 쿼리를 사용하지만, **컴파일은 한 번만 하면 되므로 성능상 이점**이 있다.

쿼리에서 **parameterized 하고 싶은 부분을 ? (물음표)로 작성**하고, 해당 부분에 들어갈 **파라미터는 PreparedStatement 의 함수를 이용해서 세팅**한다.

- 주요 메소드
    - `public void setInt(int paramIndex, int value)`
        
        paramIndex 자리에 있는 파라미터에 int 값으로 세팅한다.
        
    - `public void setString(int paramIndex, String value)`
        
        paramIndex 자리에 있는 파라미터에 String 값으로 세팅한다.
        
    - `public void setFloat(int paramIndex, float value)`
        
        paramIndex 자리에 있는 파라미터에 float 값으로 세팅한다.
        
    - `public void setDouble(int paramIndex, double value)`
        
        paramIndex 자리에 있는 파라미터에 double 값으로 세팅한다.
        

조금 복잡하다.