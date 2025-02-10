class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        # Reverse each row
        for i in image:
            i.reverse()
        # Invert the image
        for i in image:
            for j in range(len(i)):
                if i[j] == 1:
                    i[j] = 0
                else:
                    i[j] = 1
        return image


        