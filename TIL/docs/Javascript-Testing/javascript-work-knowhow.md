---

## js, jsx 차이

- 221226, resilience session

-   jsx는 JavaScript 확장 문법
	-   JavaScript안에서 `HTML 사용 가능`
-   jsx 사용이 필수는 아니지만 추천 (리액트 공식 홈페이지 - 문서 - JSX 소개 탭)
![](https://blog.kakaocdn.net/dn/FxoUT/btrwdlN1r08/bKsqYKG0akkC7luwPLDws0/img.png)
-   기능적인 차이는 없으나 팀 내 협의의 문제
- 코드에서의 차이
	- js
	```javascript
	// JS
	class Hello extends React.Component {
	  render() {
	    return React.createElement("div", null, "Hello ", this.props.name);
	  }
	}

	ReactDOM.render(
	  React.createElement(Hello, {name: "World"}),
	  document.getElementById('container')
	);
	```
	- jsx
	```javascript
	// JSX
	class Hello extends React.Component {
	  render() {
	    return <div>Hello {this.props.name}</div>;
	  }
	}

	ReactDOM.render(
	  <Hello name="World" />,
	  document.getElementById('container')
	);
	```
---

# javascript와 node.js 차이점

- 221226, resilience session

## 개요
- JavaScript : `client`에 대한 개발을 하는 도구
- nodejs : backend에서 `server`에 대한 개발을 하는 도구

## 상세 내용
- nodejs는 chrome의 자바스크립트 엔진인 v8을 이용
- 자바 스크립트는 스크립트 언어로써 `브라우저`에서만 사용가능한데 nodejs를 통하여 브라우저 없이도 실행을 할수 있게 됨.
- JavaScript를 크롬(Chrome)같은 브라우저에서만 쓰는 것이 아닌 브라우저 밖. 즉, 내 컴퓨터에서 다양한 용도로 확장하기 위해 만들어진 것이 바로 Node.js이다.

---


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMDY4ODU4MjAsNTM3MTM2NDg4LDYxMj
A0NDM1OV19
-->