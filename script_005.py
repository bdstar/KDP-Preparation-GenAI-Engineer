import matplotlib.pyplot as plt
 
fig, ax = plt.subplots()
ax.plot(range(len(losses)), losses)
ax.set_xlabel("training step")
ax.set_ylabel("loss")
ax.set_title("Training loss")
fig.savefig("loss.png", dpi=150)
