# Maximum Sum BST

msum=0
def f(root):
    if not root:
        return 10**5, -10**5,0
    lmin,lmax,lsum = f(root.left)
    rmin,rmax,rsum=f(root.right)

    if lmax<root.val<rmin:
        global msum
        msum=max(msum,lsum+rsum+root.val)
        return min(lmin,root.val),max(rmax,root.val),lsum+rsum+root.val
    return -10**5,10**5,0

def solve(root):
    global msum
    msum=0
    f(root)
    return msum
