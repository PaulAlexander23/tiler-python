import sys
import ctypes
from sdl2 import *
from sdl2.sdlimage import *


def toArray(tile_list, tile_type):
    tile_array = []
    for j in range(len(tile_array)):
        for i in range(len(tile_array(j))):
            if tile_array[j][i] == tile_type:
                tile_list.append([i, j])


def toList(tile_array, tile_type):
    tile_list = []
    for j in range(len(tile_array)):
        for i in range(len(tile_array(j))):
            if tile_array[j][i] == tile_type:
                tile_list.append([i, j])


def myDst(nX, nY):
    cW = 80
    cH = 80
    x = nX * cW
    y = nY * cH
    return SDL_Rect(x, y, cW, cH)


def myClip(n):
    cW = 80
    cH = 80
    x = int(n / 3) * cW
    y = n % 3 * cH
    return SDL_Rect(x, y, cW, cH)


def main():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(b"Hello world",
                             SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                             592, 460, SDL_WINDOW_SHOWN)
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC)
    image = IMG_LoadTexture(renderer, b"tiles.bmp")

    dst = SDL_Rect(0, 0)
    w = ctypes.pointer(ctypes.c_int(0))
    h = ctypes.pointer(ctypes.c_int(0))
    SDL_QueryTexture(image, None, None, w, h)
    dst.w = w.contents.value
    dst.h = h.contents.value

    tiles = [[ 7, 8, 8, 8, 7, 7, 7],
             [10, 0, 0, 0, 5, 8, 7],
             [10, 0, 0, 0, 0, 0, 4],
             [10, 0, 0, 3, 9, 0, 4],
             [ 7, 6, 6, 7, 7, 6, 7]]
    lava_tiles = toList(tiles,0)
 
    running = True
    event = SDL_Event()
    while running:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                running = False
                break

        SDL_RenderClear(renderer)
        for j in range(len(tiles)):
            for i in range(len(tiles[j])):
                clip = myClip(tiles[j][i])
                dst = myDst(i, j) 
                SDL_RenderCopy(renderer, image, clip, dst)

        SDL_RenderPresent(renderer)
        
        SDL_Delay(350)
    
    SDL_DestroyTexture(image)
    SDL_DestroyRenderer(renderer)
    SDL_DestroyWindow(window)
    SDL_Quit()
    return 0

if __name__ == "__main__":
    sys.exit(main())
