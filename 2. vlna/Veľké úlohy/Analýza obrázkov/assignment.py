from enum import Enum, auto
from typing import Callable
from pathlib import Path
import numpy as np
import cv2


class Location(Enum):
    CITY = auto()
    NATURE = auto()


class PartOfDay(Enum):
    SUNRISESUNSET = auto()
    DAY = auto()
    NIGHT = auto()


class Season(Enum):
    SPRINGSUMMER = auto()
    AUTUMN = auto()
    WINTER = auto()


class Notes(Enum):
    NOTES = auto()
    NOT_NOTES = auto()


# počitanie pixelov rôznej farby
def count_of_pix(img, lower_color, upper_color):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_color, upper_color)
    pocet_pixelov = cv2.countNonZero(mask)
    # vyjadrenie pixelou podielom veľkosti obrázku
    # aby bolo jedno aká je fotka veľká
    return pocet_pixelov / (len(img) * len(img[0]) * len(img[0, 0])) * 100


# to iste ako count_of_pix
# postupom casu som prisiel na elegantnejsie riesenie...
def pix_count(img, color_lower, color_upper):
    mask = cv2.inRange(img, color_lower, color_upper)
    pocet_pixelov = cv2.countNonZero(mask)
    return round(pocet_pixelov/(len(img) * len(img[0])) * 100, 2)


# HAA - homemade AI approved xd
def classify_location(image: np.ndarray) -> Location:
    green_pixs = count_of_pix(image, (40, 40, 40), (80, 255, 255))
    print(green_pixs)
    if green_pixs > 2.39:
        return Location.NATURE
    return Location.CITY


def classify_time_of_day(image: np.ndarray) -> PartOfDay:  # HAA
    black_pixs = count_of_pix(image, (0, 0, 0), (180, 255, 30))

    yellow_pixs = count_of_pix(image, (20, 100, 100), (30, 255, 255))
    orange_pixs = count_of_pix(image, (10, 100, 100), (20, 255, 255))
    yelloworange_pixs = count_of_pix(image, (10, 100, 100), (30, 255, 255))
    color_pixs = yellow_pixs + orange_pixs + yelloworange_pixs
    if color_pixs > 0.85 and 1.02 < black_pixs < 23.57:
        return PartOfDay.SUNRISESUNSET
    if black_pixs > 13.2:
        return PartOfDay.NIGHT
    return PartOfDay.DAY


def classify_season(image: np.ndarray) -> Season:
    white_pixs = pix_count(image, (185, 175, 150), (255, 255, 225))
    green_pixs = pix_count(image, (20, 90, 55), (100, 150, 120))
    orange_pixs = pix_count(image, (0, 70, 110), (60, 160, 230))
    if orange_pixs < 0.75 and white_pixs > 18:
        return Season.WINTER
    if 2.93 < green_pixs:
        return Season.SPRINGSUMMER
    return Season.AUTUMN


def classify_notes(image: np.ndarray) -> Notes:
    white_pixs = pix_count(image, (120, 140, 150), (255, 255, 255))

    if 85 > white_pixs > 60:
        return Notes.NOTES
    return Notes.NOT_NOTES
# ----------------------------------------------------
# --- Below this line is just code that runs tests ---
# ----------------------------------------------------


def test_category(path: str,
                  function: Callable[[np.ndarray], Enum],
                  correct: Enum) -> bool:
    print(f"--- Testing {correct} classification! ---")
    print(correct)
    correctly_classified = 0
    number_of_images = 0
    for image_path in Path(path).iterdir():
        image = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
        result = function(image)
        number_of_images += 1
        if result == correct:
            correctly_classified += 1
            print(f"[âś“] Correctly classified {image_path}")
        else:
            print(f"[X] Incorrectly classified {image_path},", end=" ")
            print("should be {correct}, your function returned {result}")
    print("Correctly classified", end=" ")
    print(f"{correctly_classified}/{number_of_images} for category {correct}")
    return correctly_classified == number_of_images


def main() -> None:
    # category: path, function, passed
    categories = {
        Location.NATURE: ["public_tests/nature", classify_location, False],
        Location.CITY: ["public_tests/city", classify_location, False],

        PartOfDay.SUNRISESUNSET: ["public_tests/sunrise_sunset",
                                  classify_time_of_day, False],
        PartOfDay.DAY: ["public_tests/midday", classify_time_of_day, False],
        PartOfDay.NIGHT: ["public_tests/night", classify_time_of_day, False],

        Season.SPRINGSUMMER: ["public_tests/spring_summer", classify_season,
                              False],
        Season.AUTUMN: ["public_tests/autumn", classify_season, False],
        Season.WINTER: ["public_tests/winter", classify_season, False],

        Notes.NOTES: ["public_tests/notes", classify_notes, False],
        Notes.NOT_NOTES: ["public_tests/not_notes", classify_notes, False]
    }
    for category, info in categories.items():
        info[2] = test_category(info[0], info[1], category)

    all_correct = True
    for category, info in categories.items():
        if not info[2]:
            print(f"Test for {category} failed!")
            all_correct = False

    if all_correct:
        print("All test have passed!")
    else:
        print("Some test have failed!")


if __name__ == "__main__":
    main()