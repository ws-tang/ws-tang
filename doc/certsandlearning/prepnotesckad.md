# Preparation Notes for Certified Kubernetes Application Developer (CKAD)

## Certificate Info

- Certificate Name: **Certified Kubernetes Application Developer** (CKAD)
- Issuer: [**The Cloud Native Computing Foundation**](https://www.cncf.io/)
- Certitication Exam Administrator: The Linux Foundation
- Certitication Exam [Registration Site](https://training.linuxfoundation.org/certification/certified-kubernetes-application-developer-ckad/)
- Validity: 2 years after issuance

<br/>

## Kubernates

[**Kubernetes**](https://kubernetes.io/), also known as **K8s**, is an open source system for automating deployment, scaling, and management of containerized applications.

It groups containers that make up an application into logical units for easy management and discovery. Kubernetes builds upon 15 years of experience of running production workloads at Google, combined with best-of-breed ideas and practices from the community.

- [K8s documentation](https://kubernetes.io/docs/home/)
- [K8s **kubectl** quick references](https://kubernetes.io/docs/reference/kubectl/quick-reference/)

<br/>

## Resources

### The exam

Details and resources about the CKAD exam is available at the section **Exam Details & Resources** on [the exam page](https://training.linuxfoundation.org/certification/certified-kubernetes-application-developer-ckad/) at the Linux Foundation.<br/>

### Preparations

- The Udemy course [**Kubernetes Certified Application Developer (CKAD) with Tests**](https://www.udemy.com/course/certified-kubernetes-application-developer/) by **Mumshad Mannambeth**, **KodeKloud Training**, and **Vijin Palazhi**. Note this is a paid course.
- The LinkedIn Learning course [**Certified Kubernetes Application Developer (CKAD) Cert Prep**](https://www.linkedin.com/learning/certified-kubernetes-application-developer-ckad-cert-prep/certified-kubernetes-application-developer-ckad-introduction?u=110661266) by **Pearson and Sander van Vugt** (access to this course requires a subscription to LinedIn Learning one way or another).
- [**CKAD Exercises - Dimitris-Ilias Gkanatsios**](https://github.com/dgkanatsios/CKAD-exercises)
- Notes and experience sharing from some kind people online:
  - [Jérôme Dx](https://dev.to/jdxlabs/efficient-tips-to-pass-the-ckad-exam-46l7)
  - [Lucassha Shannon](https://github.com/lucassha/CKAD-resources?tab=readme-ov-file)
  - [Michael England](https://medium.com/@michael_england/how-i-passed-the-certified-kubernetes-application-developer-ckad-exam-cd443f160643)
  - [Haripraghash Subramaniam](https://medium.com/@harioverhere/ckad-certified-kubernetes-application-developer-my-journey-3afb0901014)

<br/>

## Personal Notes

Below is my experience and notes. Hope it helps.

1. First of all, great thanks to the individuals noted above in the section **Preparations** for the resources they kindly provide and share. The info from them is very helpful to my preparation for my CKAD exam.
1. The course **Kubernetes Certified Application Developer (CKAD) with Tests** by **Mumshad Mannambeth** and company at Udemy is very helpful. They do a good job to explain K8s and provide a cloud lab environment for hands-on practice. That should give one a good understanding about K8s and know how to run its commands. For the Udemy course, it is a **paid** course. One does not need to purchase it at the full price. Wait for Udemy promotions for a much lower price. Udemy offers discounts from time to time, at least 2-3 times a month. And the offered discounts vary at different times. If one is not in a hurry, one can visit Udemy often, observe, then act.
1. In addition to the cloud lab environment from the **Mumshad Mannambeth**'s course at Udemy, I also set up my own K8s lab to practice freely. My notes for a K8s lab setup is noted [here](../../lab/k8s/kuberneteslab.md).
1. The course by **Sander van Vugt** helped me too. The instructor offers a procedure in details to set up a K8s lab with Minikube in the course. Though I didn't take that approach since I have set up my lab before seeing it.
1. The CKAD exercise provided by **Dimitris-Ilias Gkanatsios** (see above) are very very helpful (kudos to him). I used my personal k8s for the CKAD exercises listed therein.
1. K8s documentation is very good and detailed. As others have noted, one has to be very familiar with K8s documentation to find the example YAML configuration for the related setup. If one does practice the CKAD exercises from Dimitris-Ilias Gkanatsios well, one will get familiar with the K8s documentation during the process.
1. After one registers for the CKAD exam, it comes with two exam simulator sessions at Killer Shell. I strongly recommended to use it to the max. One simulation session will last **36 hours** after one activates it. So one can plan it ahead to practice over a two-day span. It allows one to do at least **two** full 2-hour simulation sessions or even three. It gives you a taste about what the actual exam environment is, which is very important and you don't get _surprise_ at the exam. My experience is that I like to set up aliases for a number of kubectl commands in my own k8s lab. However, I found out that does NOT work in the Killer Shell environment. So I had to get back to run the kubectl commands in full instead. It's good that I found this out during the simulation rather than the actual exam.
1. Someone suggested to do the whole set of CKAD exercises from Dimitris-Ilias Gkanatsios. I agree doing so will help a lot. I personally did it **3-4** times.
1. During the CKAD exam, as others strongly recommend **not to stick to one question too long if you can't solve it quickly**. Flag the question and come back to it later. When I took the exam, I had about 5 questions that I couldn't solve quickly. I flagged them and came back to them after I went through all questions. At the end, I solved all of my flagged questions with more than 20 minutes remaining.
1. Not sure that it is the proctor or the auto-monitoring, it is very strict. The exam is 120 minutes. I was warned for being _out-of-camera_ twice when I moved my body a little on my seat to loosen myself a bit. I still well sat on my seat, not like off it. I used a typical Logitech webcam. (If one gets warned for whatever reason three times, the exam will not count.) So be prepared to sit still through the exam.
