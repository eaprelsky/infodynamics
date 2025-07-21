# Shannon's Information Revolution (1948)

*The discovery that changed how we understand information itself*

---

Picture this: It's 1948, and Claude Shannon is working at Bell Labs, trying to solve a very practical problem. Telephone calls are expensive, and the company wants to know the most efficient way to send messages through their wires. Shannon asks himself a deceptively simple question: "How much information does a message actually contain?"

To answer this, Shannon imagines you're waiting for a message. If someone tells you "the sun will rise tomorrow," that message contains almost no useful information because you already knew that would happen. But if someone tells you "it's snowing in the Sahara Desert right now," that message is packed with information because it's completely unexpected.

This insight led Shannon to a remarkable discovery. He realized that the amount of information in a message depends entirely on how surprising it is. The more unexpected something is, the more information it carries. Shannon captured this relationship in a simple mathematical formula:

$$I(x) = -\log_2 p(x)$$

where I(x) represents the information content and p(x) represents how likely the event is to happen.

Let's unpack what this formula actually means by walking through some examples. Imagine you flip a fair coin. The probability of getting heads is exactly 50%, or 0.5 in mathematical terms. If we plug this into Shannon's formula, we get: I(heads) = -log₂(0.5) = 1 bit. This means a coin flip gives you exactly one bit of information.

Now consider rolling a six-sided die and trying to predict which number will come up. Each number has a 1-in-6 chance, or about 0.167 probability. Shannon's formula tells us this carries about 2.6 bits of information—more than a coin flip because there are more possible outcomes to distinguish between.

But here's where it gets really interesting. Think about winning the lottery with odds of 1 in 100 million. That probability is 0.00000001, and Shannon's formula says such an event carries about 26.6 bits of information. Compare that to the sun rising tomorrow, which has a probability so close to 1 that it carries virtually zero bits of information.

The genius of Shannon's formula lies in its mathematical structure. He chose the logarithm function because it has a special property: when independent events happen together, their information content simply adds up. If you flip a coin twice, the total information is 1 bit + 1 bit = 2 bits. This additive property makes the formula incredibly useful for analyzing complex communication systems.

Shannon used base-2 logarithms because they naturally measure information in "bits"—each bit represents one yes-or-no decision. The negative sign might seem strange at first, but it's there because logarithms of numbers less than 1 are negative, and Shannon wanted information content to always be positive.

What Shannon didn't realize at the time was that he had stumbled upon something much deeper than telecommunications theory. His formula describes how our brains actually process information. When something unexpected happens—like hearing surprising news or encountering an unusual situation—our cognitive systems respond more strongly. The rare, unexpected events demand more mental energy and attention, just as Shannon's formula predicts they should carry more information.

This connection between mathematical information theory and human cognition became one of the first clues that our minds might operate according to electrical principles. In our information physics framework, Shannon's formula becomes the foundation for what we call "information voltage"—the driving force that pushes information through cognitive circuits.

The surprise component of information voltage follows exactly the same mathematical relationship Shannon discovered:

$$U_{\text{surprise}} = -\log_2 p(\text{message})$$

When your brain encounters unexpected information, it creates high cognitive voltage, just like unexpected electrical signals create high voltage in electronic circuits. This isn't just a metaphor—modern neuroscience has confirmed that surprising stimuli actually generate stronger electrical responses in brain tissue.

Shannon's 1948 discovery, originally intended to optimize telephone networks, turned out to reveal fundamental principles about how information creates electrical pressure in any system that processes it—including the human mind. His mathematical insight bridges the gap between the abstract concept of "information" and the physical reality of electrical circuits, providing the first piece of evidence that consciousness itself might be an electrical phenomenon.

Recent neuroscience research reveals that Shannon's mathematical principle has direct biological implementation in the brain. Neurons respond more strongly to unexpected stimuli, creating a biological "information voltage" that directly parallels Shannon's mathematical formulation. The brain automatically allocates more attentional resources to high-information-content stimuli, explaining why unexpected events capture our attention. High-information events are more likely to be encoded in long-term memory, suggesting that biological memory systems implicitly implement Shannon's information measure.

This biological validation of Shannon's mathematical insight provides strong evidence for the electrical nature of information processing in cognitive systems. What started as a practical solution to telephone engineering problems became the mathematical foundation for understanding consciousness itself.

**🔗 Interactive Exploration:** [Shannon Information Calculator](../demos/notebooks/shannon_demo.ipynb) - Experiment with different probabilities and see how information content changes.

---

*Next: How Miller discovered the electrical "capacitance" of human memory...* 