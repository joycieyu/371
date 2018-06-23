# creating data
set.seed(2)
x=matrix(rnorm(50*2), ncol=2)
x[1:25,1]=x[1:25,1]+3
x[1:25,2]=x[1:25,2]-4

# kmeans for k=2
km.out=kmeans(x,2,nstart=20)

km.out$cluster

# plot original color
plot(x)

# plot w/ kmeans assignments and COLOR!
plot(x, col=(km.out$cluster+1), main="K-Means Clustering Results with K=2", ylab="", pch=20, cex=2)


set.seed(4)
# kmeans for k=3
km.out=kmeans(x,3,nstart=20)


set.seed(3)
# kmeans for k=3
km.out=kmeans(x,3,nstart=1)
km.out$tot.withinss
km.out$cluster

# plot original color
plot(x)

# plot w/ kmeans assignments and COLOR!
plot(x, col=(km.out$cluster+1), main="K-Means Clustering Results with K=3", ylab="", pch=20, cex=2)




hc.complete= hclust(dist(x), method="complete")
plot(hc.complete, main = "complete Linkage", xlab="", sub="", cex=0.9)



hc.average= hclust(dist(x), method="average")
hc.single= hclust(dist(x), method="single")

plot(hc.average, main = "average Linkage", xlab="", sub="", cex=0.9)
plot(hc.single, main = "single Linkage", xlab="", sub="", cex=0.9)


cutree(hc.complete,2)
cutree(hc.average,2)
cutree(hc.single,2)




