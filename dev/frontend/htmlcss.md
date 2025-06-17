# HTML and CSS Dev Notes

**Table of Contents**

- [HTML](#fe_html)
- [CSS](#fe_css)

<br/>

## HTML <a name="fe_html"></a>

### HTML Metadata Cheat Sheet

[Source](https://www.coursera.org/learn/html-and-css-in-depth/supplement/8QDS1/metadata-cheat-sheet)

<span style="text-decoration:underline">HTML `<meta>` tags</span>

**Name**

The name of the property can be anything you like, although browsers usually expect a value they understand and can take an action upon. An example would be `<meta name="author" content="name">` to state the author of the page.

**Content**

The content field specifies the property's value. For example, you can use `<meta name="language" content="english">`, to specify the language of the webpage to search engines.

**Charset**

The charset is a special field that lets you specify the character encoding used for the page so that the browser can display it properly. The most frequently used is utf-8, and you would add it to your HTML header as follows: `<meta charset="UTF-8">`

**HTTP-equiv**

This field stands for HTTP equivalent, and it’s used to simulate HTTP response headers. This is rare to see, and it’s recommended to use HTTP headers over HTML http-equiv meta tags. For example, the next tag would instruct the browser to refresh the page every 30 minutes: `<meta http-equiv="refresh" content="30">`

<span style="text-decoration:underline">Basic meta tags (meta tags For SEO)</span>

`<meta name="description"/>` provides a brief description of the web page

`<meta name=”title”/>` specifies the title of the web page

`<meta name="author" content="name">` specifies the author of the web page

`<meta name="language" content="english">` specifies the language of the web page

`<meta name="robots" content="index,follow" />` tells search engines how to crawl or index a certain page

`<meta name="google"/>` tells Google not to show the sitelinks search box for your page when showing search results

`<meta name="googlebot" content=”notranslate” />` tells Google you don’t want to provide an automatic translation for your page if the user uses a different language

`<meta name="revised" content="Sunday, July 18th, 2010, 5:15 pm" />` specifies the last modified date and time on which you have made certain changes

`<meta name="rating" content="safe for kids">` specifies the expected audience for your page

`<meta name="copyright" content="Copyright 2022">` specifies a Copyright

<span style="text-decoration:underline">`<meta http-equiv="..."/>` tags</span>

`<meta http-equiv="content-type" content="text/html">` specifies the format of the document returned by the server

`<meta http-equiv="default-style"/>` specifies the format of the styling document

`<meta http-equiv="refresh"/>` specifies the duration of the page before it’s considered stale

`<meta http-equiv=”Content-language”/>` specifies the language of the page

`<meta http-equiv="Cache-Control" content="no-cache">` instructs the browser how to cache your page
Responsive design/mobile meta tags

`<meta name="format-detection" content="telephone=yes"/>` indicates that telephone numbers should appear as hypertext links that can be clicked to make a phone call

`<meta name="HandheldFriendly" content="true"/>` specifies that the page can be properly visualized on mobile devices

`<meta name="viewport" content="width=device-width, initial-scale=1.0"/>` specifies the area of the window in which web content can be seen

### `<script>` Tag Location

- Generally, place `<script>` tags just before the closing `</body>` tag for better performance and to ensure the DOM is ready for manipulation.
- Consider placing **core** scripts or scripts that need to run before page rendering in the `<head>` section.
- For scripts in the `<head>`, consider using **async** or **defer** attributes to prevent blocking rendering.

Ultimately, the best placement depends on the specific script and its functionality. Experimentation and performance testing can help determine the optimal location for your scripts

### Open Graph Metadata Tags

Open Graph metadata tags reside in the `<head>` section and there are four required Open Graph metadata tags if in use.

- `og:title`
- `og:type`
- `og:url`
- `og:image`

### Client-side Validation

- [HTML5 Form Validation Examples](https://www.the-art-of-web.com/html/html5-form-validation/)
- [Client-Side Form Validation with HTML5](https://www.sitepoint.com/client-side-form-validation-html5/)

### References

- [Semantic HTML cheat sheet](https://dev.to/sabeerjuniad/semantic-html-cheat-sheet-3be9)

<br/>

## CSS <a name="fe_css"></a>

- [CSS Layout](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout)
- [CSS Values and Units](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units)
- [CSS Box Model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model)
- [List of Deprecated Attributes Still in Widespread Use ](https://css-tricks.com/list-of-depreciated-elements-still-in-widespread-use/)

### Flexbox

<span style="text-decoration:underline;font-weight:bold">References<span>

- [CSS Flexbox Layout Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [Flex Cheatsheet](https://yoksel.github.io/flex-cheatsheet/) by Yoksel
- [CSS Flexbox Tutorial with Flexbox Properties Cheat Sheet](https://www.freecodecamp.org/news/css-flexbox-tutorial-with-cheatsheet/)

### Grid

Grid areas are a way to group one or more grid cells. The grid template area is an extension of this concept where you can give names to these grid areas. Once you have the names defined, you can address these new grid area items by their names and configure them accordingly.

The property grid-template-areas is usually placed inside the body tag or any container where the grid needs to be placed, the same way that you would define the rules for the grid. The main difference is, in case of grid-template-areas the values present will be the different names.
Process

The process isn’t prescriptive but these are the steps in general:

1. Define the grid using display property
1. Set the height and width of the grid
1. Set the grid-template-areas with the appropriate name identifiers
1. Add the appropriate sizes for the rows inside the grid using grid-template-rows property
1. Add the appropriate sizes for the columns inside the grid using grid-template-columns property

But how exactly do you use these names and where do they come from? The names that you use inside the grid template areas are the HTML tags that you have used. Or, where you need to get more specific, you designate a class name to these tags. Once the names are assigned, you define the properties for each class the same way that you define them conventionally.

<span style="text-decoration:underline;font-weight:bold">References<span>

- [CSS Grid Layout Guide](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [Complete CSS Grid Tutorial with Cheat Sheet](https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/)
- [Learn CSS Grid](https://learncssgrid.com/)
- [Grid](https://web.dev/learn/css/grid/)
- [CSS Viewport](https://www.educba.com/css-viewport/) (for mobile devices)

### CSS Units and Measurements

<span style="text-decoration:underline;font-weight:bold">Absolute<span>

| Unit | Name                | Comparison               |
| ---- | ------------------- | ------------------------ |
| Q    | Quarter-millimeters | 1Q = 1/40th of 1cm       |
| mm   | Millimeters         | 1mm = 1/10th of 1cm      |
| cm   | Centimeters         | 1cm = 37.8px = 25.2/64in |
| in   | Inches              | 1in = 2.54cm = 96px      |
| pc   | Picas               | 1pc = 1/6th of 1in       |
| pt   | Points              | 1pt = 1/72nd of 1in      |
| px   | Pixels              | 1px = 1/96th of 1in      |

<span style="text-decoration:underline;font-weight:bold">Relative<span>

| Unit | Description and relativity                                      |
| ---- | --------------------------------------------------------------- |
| em   | Font size of the parent where present.                          |
| ex   | x-co-ordinate or height of the font element.                    |
| ch   | Width of the font character.                                    |
| rem  | Font size of the root element.                                  |
| lh   | Value computed for line height of parent element.               |
| rlh  | Value computed for line height of root element which is <html>. |
| vw   | 1% of the viewport width.                                       |
| vh   | 1% of the viewport height.                                      |
| vmin | 1% of the smaller dimension of viewport.                        |
| vmax | 1% of the larger dimension of viewport.                         |
| %    | Denotes a percentage value in relation to its parent element.   |

### Selectors

**Quick References**

- [Commonly used selectors](https://www.geeksforgeeks.org/10-css-selectors-every-developer-should-know/)
- [Combinator selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Combinators)
- [Comprehensive list of pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)
- [Comprehensive list of pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements)

Standard CSS selectors:

- Element or type
- Id
- Class
- Attribute
- nth-of-type and nth-of-child

Specificity hierarchy

CSS has a set of rules that it uses to ‘score’ or assign a certain weight to selectors and this creates a specificity hierarchy. Based on the weights, there are four categories in this hierarchy (in priority):

| Priority | Category                                | Assigned Value | Example                                  |
| -------- | --------------------------------------- | -------------- | ---------------------------------------- |
| 1        | Inline styles                           | 1000           |  `<p style=“color: white;”>`             |
| 2        | IDs                                     | 100            | `#div`                                   |
| 3        | Classes, attributes, and pseudo-classes | 10             | `.my-class` `p[“attribute”]` `div:hover` |
| 4        | Elements and pseudo-elements            | 1              | `div`                                    |

Examples:

`p#bar` => 1 element & 1 ID => 0 1 0 1 => Score: 101

`p.foo` => 1 element & 1 class => 0 0 1 1 => Score: 11

`p.p.foo` => 1 element & 2 class => 0 0 2 1 => Score: 21

### Combination Selectors

| Priority | Type             | Symbol      |
| -------- | ---------------- | ----------- |
| 1        | Descedant        | using space |
| 2        | Child            | `>`         |
| 3        | General sibling  | `~`         |
| 4        | Adjacent sibling | `+`         |

### Pseudo-class Selectors

```
selector:pseudo-class {
    property: value;
}
```

Some quick ones are listed below. See [CSS Psudo Class Cheat Sheet](./CSS_PseudoClass_CheatSheet.pdf) for more details.

| Type                 | pseudo-classes                  |
| -------------------- | ------------------------------- |
| Action State         | `:hover`                        |
| Action State         | `:active`                       |
| Action State         | `:focus`                        |
| Form                 | `:disabled` and `enabled`       |
| Form                 | `:checked` and `:indeterminate` |
| Form                 | `:valid` and `:invalid`         |
| Position-based state | `:first-of-type`                |
| Position-based state | `:last-of-type`                 |
| Position-based state | `:nth-of-type`                  |
| Position-based state | `:nth-last-of-type`             |
| Popular              | `::first-letter`                |
| Popular              | `::first-line`                  |
| Popular              | `::selection`                   |
| Popular              | `::marker`                      |
| Popular              | `::before` and `::after`        |

--

For web links, apply pseudo-class in the order of LVHA: **Link**, **Visited**, **Hover**, and **Active**.

### Effect

A change which is a result or consequence of an action or other cause.

Some common effects include: Animation (graphics in motion transitioning over time), Hover, Cursor, Sliding, Video, Parallax, Back-to-Top, Element and Color Transitions, Full Screen Snapping

- `transform` property: modify the spacial position of an element
- `transition` property: control the speed of the occuring effect (used with `transform`)

- [Transform and transition property](https://www.lambdatest.com/blog/css-transforms-and-transitions-property/)
- [Detailed information about @keyframes](https://developer.mozilla.org/en-US/docs/Web/CSS/@keyframes)

### Linting Tool

If using MS VS Code, one can consider to add the extension **Stylelint** to normalize the CSS code within VS Code.

### Debugging

- [How to tackle CSS specificity issues and when to use the !important keyword](https://www.freecodecamp.org/news/how-to-tackle-css-specificity-issues-and-when-to-use-the-important-keyword-b54123995e1a/)
- [12 Common CSS Mistakes Web Developers Make](https://www.webfx.com/blog/web-design/12-common-css-mistakes-web-developers-make/)

<br/>
