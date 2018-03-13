Title: Route Leaks Identification by Detecting Routing Loops,  SecureComm2015
Date: 2015-10-28 12:50
Author: duanhx
Tags: Papers, BGP, MITM
Slug: route-leaks-identification-by-detecting-routing-loops-securecomm2015

`Song Li, Haixin Duan, Zhiliang Wang, and Xing Li, Tsinghua University`

###Abstract
Route leaks have become an important security problem of inter-domain routing. Operators increasingly suffer from large-scale or small-scale route leak incidents in recent years. Route leaks can redirect traffic to unintended networks, which puts the traffic at risk of Man-in- the-Middle attack. Unlike other security threats such as prefix hijacking that advertises bogus BGP route, route leaks announce routes which are true but in violation of routing policies to BGP neighbors. Since the routing policies are usually kept confidential, detecting route leaks in the Internet is a challenging problem. In this paper, we reveal a link between routing loops and route leaks. We find that some route leaks may cause routing loops. Hence detecting routing loops is expected to be able to identify route leaks. We provide theoretical analysis to confirm the expectation, and further propose a detection mechanism which can identify the leaked route as well as the perpetrator AS. Our mechanism does not require information about routing policies. It passively monitors BGP routes to detect route leaks and hence it is lightweight and easy to deploy. The evaluation results show that our mechanism can detect a lot of route leaks that occur in the Internet per day.

###Key words: 
AS relationship, Routing policies, Route leaks, Routing loops, Identification
