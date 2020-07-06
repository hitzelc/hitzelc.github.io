from random import sample
import numpy as np
import os
from PIL import Image
from sklearn.cluster import KMeans
import time

'''
Make sure you go ahead and define an image directory to read from on line 42,
and a place to save your images on line 88
'''

def connectedComponents(clustered_array):
    def bound(num):
        #bound the neighbors so that the edges of the image do not wrap around.
        return max(min(num,299),0)
    labelled_locations = set()
    label = 0
    queue = []
    clustered_arrayshape = clustered_array.shape
    labelled_array = np.zeros(clustered_arrayshape)
    for r in range(clustered_arrayshape[0]):
        for c in range(clustered_arrayshape[1]):
            label += 1
            if (r,c) not in labelled_locations and clustered_array[(r,c)][0]:
                labelled_array[(r,c)] = label
                labelled_locations.add((r,c))
                queue.append((r,c))
                while len(queue):
                    q = queue.pop()
                    neighbors = [(bound(q[0]+1),bound(q[1]+1)),(bound(q[0]+1),q[1]),(bound(q[0]+1),bound(q[1]-1)),(bound(q[0]-1),bound(q[1]+1)),(bound(q[0]-1),q[1]),(bound(q[0]-1),bound(q[1]-1)),(q[0],bound(q[1]+1)),(q[0],bound(q[1]-1))]
                    for n in neighbors:
                        if n not in labelled_locations and clustered_array[n][0]:
                            labelled_array[n] = label
                            labelled_locations.add(n)
                            queue.append(n)
                        else:
                            continue
            else:
                continue
    return labelled_array

def main():
    #you'll need your own directory here
    image_directory = ''
    #I make use of a list of English words
    #you could just sample from the image titles or take user input
    #you could even hard code some strings
    with open('words_alpha.txt','r') as f:
        words = f.read().split()
    words_to_search = sample(words,1500)
    for search_word in words_to_search:
        found_images = []
        for i in os.listdir(image_directory):
            searchstrs = search_word.split()
            for searchstr in searchstrs:
                if searchstr.lower() in i.lower():
                    try:
                        img = Image.open(image_directory+'/'+i).convert('RGB')
                    except OSError:
                        continue
                    arr = np.array(img)
                    found_images.append(arr)
                else:
                    continue
        if len(found_images) <= 1:
            continue
        generated_image = np.zeros((300,300,3),np.uint8)
        cycle_number = 0
        while np.count_nonzero(generated_image[:,:,0]+generated_image[:,:,1]+generated_image[:,:,2]) < 300*300 and cycle_number < 200:
            this_k = np.random.randint(5,10)
            km = KMeans(n_clusters=this_k)
            random_image = found_images[np.random.randint(0,len(found_images))]
            array_for_clustering = random_image.reshape((random_image.shape[0]*random_image.shape[1],3))
            km.fit(array_for_clustering)
            clustered_image = km.predict(array_for_clustering)
            clustered_image = clustered_image.reshape((random_image.shape[0],random_image.shape[1]))
            chosen_cluster = np.atleast_3d(clustered_image == np.random.randint(0,this_k))
            connected_clusters = connectedComponents(chosen_cluster)
            largest_connected_cluster = np.unique(connected_clusters,return_counts=True)[0][np.argwhere(np.unique(connected_clusters,return_counts=True)[1] == max(np.unique(connected_clusters,return_counts=True)[1][1:]))]
            chosen_connected_cluster = np.atleast_3d(connected_clusters == largest_connected_cluster)
            connected_cluster_from_image = random_image*chosen_connected_cluster
            empty_pixels = np.atleast_3d((generated_image[:,:,0]+generated_image[:,:,1]+generated_image[:,:,2]) == 0)
            final_pixels = connected_cluster_from_image*empty_pixels
            generated_image += final_pixels
            cycle_number += 1
        thisimagename = search_word+'_'+str(time.time())
        generated_image_PIL = Image.fromarray(generated_image)
        #you will need a directory to save the images to
        generated_image_PIL.save(thisimagename+'.png')
main()