# React.js Dev Notes

Here are my notes for React.js related topics.

**Table of Contents**

- [Development Setup](#dev_setup)
- [React](#reactjs)
- [Bootstrap](#bootstrapcss)
- [References](#references)

<br/>

## Development Setup <a name="dev_setup"></a>

<br/>

## React.js <a name="reactjs"></a>

React offcial [site](https://reactjs.org/)

React builds a representation of the browser Document Object Model (**DOM**) in memory called the **virtual DOM**. As components are updated, React checks to see if the component’s HTML code in the virtual DOM matches the browser DOM. If a change is required, the browser DOM is updated. If nothing has changed, then no update is performed.

This is called the _reconciliation_ process and can be broken down into the following steps:

1. The virtual DOM is updated.
1. The virtual DOM is compared to the previous version of the virtual DOM and checks which elements have changed.
1. The changed elements are updated in the browser DOM.
1. The displayed webpage updates to match the browser DOM.

<br/>

## Bootstrap <a name="bootstrapcss"></a>

[**Bootstrap**](https://getbootstrap.com/) is a _library_ of CSS and JavaScript code that you can combine to quickly build visually appealing websites.

Modern web development is all about **components**. Small pieces of reusable code that allow you to build websites quickly. Bootstrap comes with multiple components for very fast construction of multiple components, or parts of components.

Another important aspect of modern development is **responsive grids** which allow web pages to adapt their layout and content depending on the device in which they are viewed. Bootstrap comes with a pre-made set of CSS rules for building a responsive grid.

Bootstrap is very popular amongst developers as it saves development time and provides a way for developers to build visually appealing prototypes and websites.

Bootstrap saves significant time because all the CSS code that styles its grid and pre-built components is already written. Instead of needing a high level of expertise in various CSS concepts, you can simply use the existing Bootstrap CSS classes to create visually appealing websites. This is indispensable when you need to quickly iterate on website layouts. ([Source](https://www.coursera.org/learn/introduction-to-front-end-development/supplement/EZ1Eu/bootstrap).)

Use Bootstrapt CDN reference for CSS

```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4Q6Gf2aSP4eDXB8Miphtr37CMZZQ5oXLH2yaXMJ2w8e2ZtHTl7GptT4jmndRuHDT" crossorigin="anonymous">
```

Use Bootstrapt CDN reference for JavaScript

```
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/js/bootstrap.bundle.min.js" integrity="sha384-j1CDi7MgGQ12Z7Qab0qlWQ/Qqz24Gc6BM0thvEMVjHnfYGF0rmFCozFSxQBxwHKO" crossorigin="anonymous"></script>
```

<br/>

## References <a name="references"></a>

- [HTML Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) by **Mozilla**
- [CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) by **Mozilla**
- [HTML and CSS: Design and build websites](https://www.amazon.com/HTML-CSS-Design-Build-Websites/dp/1118008189/) by Jon Duckett
- [Responsive Web Design with HTML5 and CSS](https://www.amazon.com/Responsive-Web-Design-HTML5-CSS/dp/1839211563/) Book by Ben Frain

<br/>
