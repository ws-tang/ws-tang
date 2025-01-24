# System Design and Software Development

**Table of Contents**

- [System Design](#sysdesign)
  - [Tutorials and references](#sysdesign_tutorials)
  - [Objectives of Systems Design](#sysdesign_objectives)
  - [Requirements](#sysdesign_requirements)
  - [Models Used for System Design Life Cycle](#sysdesign_models")
- [Software Development Life Cycle (SDLC)](#swdev)

<br/>

## System Design <a name="sysdesign"></a>

### Tutorials and references <a name="sysdesign_tutorials"></a>

- [The System Design Primer](https://github.com/donnemartin/system-design-primer?tab=readme-ov-file) by Donne Martin
- [How To Prepare For a System Design Interview](https://interviewing.io/guides/system-design-interview#what-this-guide-is-and-whom-it-s-for) by interviewing.io
- [System Design Tutorial](https://www.geeksforgeeks.org/system-design-tutorial/) by Geeks for Geeks

### Objectives of Systems Design <a name="sysdesign_objectives"></a>

Below are the main objectives of Systems Design:

- **Practicality**: We need a system that should be targetting the set of audiences(users) corresponding to which they are designing.
- **Accuracy**: Above system design should be designed in such a way it fulfills nearly all requirements around which it is designed be it functional or non-functional requirements.
- **Completeness**: System design should meet all user requirements
- **Efficient**: The system design should be such that it should not overuse surpassing the cost of resources nor under use as it will by now we know will result in low thorough put (output) and less response time(latency).
- **Reliability**: The system designed should be in proximity to a failure-free environment for a certain period of time.
- **Optimization**: Time and space are just likely what we do for code chunks for individual components to work in a system.
- **Scalable(flexibility)**: System design should be adaptable with time as per different user needs of customers which we know will keep on changing on time.

Some of the major advantages of System Design include:

- **Reduces the Design Cost of a Product**: By using established design patterns and reusable components, teams can lower the effort and expense associated with creating new software designs.
- **Speedy Software Development Process**: Using frameworks and libraries accelerates development by providing pre-built functionalities, allowing developers to focus on unique features.
- **Saves Overall Time in SDLC**: Streamlined processes and automation in the Software Development Life Cycle (SDLC) lead to quicker iterations and faster time-to-market.
- **Increases Efficiency and Consistency of a Programmer**: Familiar tools and methodologies enable programmers to work more effectively and produce uniform code, reducing the likelihood of errors.
- **Saves Resources**: Optimized workflows and shared resources minimize the need for redundant efforts, thereby conserving both human and material resources.

([Source](https://www.geeksforgeeks.org/what-is-system-design-learn-system-design/))

### Requirements <a name="sysdesign_requirements"></a>

Requirements may be divided into three categories: **Functional Requirements**, **Non-Functional Requirements**, and **Extended Requirements**.

<span style="text-decoration:underline">Functional Requirements</span>

These are the requirements that the end users specifically demand as the functionalities that MUST exist in the final product or solution when delivered. Examples are:

- What are the features that we need to design for this system?
- What are the edge cases we need to consider, if any, in our design?

<span style="text-decoration:underline">Non-Functional Requirements</span>

These are the quality constraints that the system MUST satisfy in additional to the functional requirements. They deal with issues like:

- Portability
- Security
- Maintainability
- Reliability
- Scalability
- Performance
- Reusability
- Flexibility

Examples are:

- Each request should be processed with the minimum latency?
- System should be highly valuable.

<span style="text-decoration:underline">Extended Requirements</span>

Extended requirements are "nice to have" or optional requirements that might get implemented should the resources allow. Examples are:

- The system should record metrices and analytics.
- Service heath and performance monitoring.

### Models Used for System Design Life Cycle <a name="sysdesign_models"></a>

Below are some models used for System Design Life Cycle:

- **Waterfall Model**: A linear and sequential model where each phase must be completed before moving on to the next. It's a straightforward approach but can be inflexible in the face of changing requirements.
- **Iterative Model**: Involves repeating cycles, with each iteration refining and improving the system based on feedback. It's adaptable to changing requirements.
- **Prototyping Model**: Involves building a prototype (a preliminary version) of the system to gather feedback refine the design before building the final product.
- **Spiral Model**: Incorporates elements of both iterative and prototyping models. It involves cycles of planning, designing, constructing, and evaluating.
- **Agile Model**: Emphasizes flexibility and collaboration, with frequent iterations and continuous feedback. It's well suited for projects where requirements may evolve.

My experience is that mix of the above models more or less seems more often than people think even though they say they are using a specific model for development. It also depends on the need and circumstances during the development and we pick a main model and adopt accordingly.

([Source](https://www.geeksforgeeks.org/system-design-life-cycle-phases-models-and-use-cases/#models-used-for-system-design-life-cycle))

<br/>

## Software Development Life Cycle (SDLC) <a name="swdev"></a>

The typical steps for a solution in a software development cycle are:

1. Define the requirements.
2. Determine the functional specifications.
3. Work on design and implementation (high-level and detailed designs).
4. Testing and verification.
5. Documentation (user guides and release notes)
6. Sustaining
   - Releases of minor updates, including enhancements and bug fixes
   - Hotfixes of high-priority bug fixes

<br/>
