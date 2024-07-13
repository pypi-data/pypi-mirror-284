from PIL import Image, ImageDraw, ImageFont
import os
from typing import List, Tuple


class Visualist:
    def __init__(self, cell_size=64, space=32):
        self.CELL_SIZE = cell_size
        self.SPACE = space
        font_path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "fonts", "Roboto-Medium.ttf"
        )
        self.font = ImageFont.truetype(font_path, int(self.CELL_SIZE / 2))

    def create_image(self, size: Tuple[int, int]) -> Image:
        return Image.new("RGBA", size, (255, 255, 255, 255))

    def draw_text_centered(
        self,
        draw: ImageDraw,
        box: Tuple[int, int, int, int],
        text: str,
        font: ImageFont,
        color=(255, 255, 255, 255),
    ):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        box_width = box[2] - box[0]
        box_height = box[3] - box[1]
        text_x = box[0] + (box_width - text_width) / 2
        text_y = box[1] + (box_height - text_height) / 2 - bbox[1]
        draw.text((text_x, text_y), text, font=font, fill=color)

    def img_from_list(
        self,
        L: List[int],
        highlight_indexes: List[int] = [],
        image_size: Tuple[int, int] = None,
        color=(36, 116, 191, 255),
        highlight_color=(255, 46, 52, 255),
        show_indexes=True,
        matrix=False,
    ) -> Image:
        start_of_drawing = (len(L) / 2) * (self.CELL_SIZE + self.SPACE)
        if image_size:
            IMAGE_SIZE = image_size
        elif matrix:
            IMAGE_SIZE = (int(2 * start_of_drawing), int(self.CELL_SIZE + self.SPACE))
        else:
            IMAGE_SIZE = (int(2 * start_of_drawing), int(3 * self.CELL_SIZE))

        img = self.create_image(IMAGE_SIZE)
        draw = ImageDraw.Draw(img)
        MIDDLE = (img.size[0] / 2, img.size[1] / 2)
        pointer = MIDDLE[0] - start_of_drawing + self.SPACE / 2

        for index, item in enumerate(L):
            X0, X1 = pointer, pointer + self.CELL_SIZE
            rect_color = highlight_color if index in highlight_indexes else color
            box = [
                (X0, MIDDLE[1] - self.CELL_SIZE / 2),
                (X1, MIDDLE[1] + self.CELL_SIZE / 2),
            ]
            draw.rectangle(box, fill=rect_color)

            self.draw_text_centered(
                draw,
                (
                    X0,
                    MIDDLE[1] - self.CELL_SIZE / 2,
                    X1,
                    MIDDLE[1] + self.CELL_SIZE / 2,
                ),
                str(item),
                self.font,
            )

            if show_indexes:
                index_box = (
                    X0,
                    MIDDLE[1] - self.CELL_SIZE - self.CELL_SIZE / 2,
                    X1,
                    MIDDLE[1] - self.CELL_SIZE / 2,
                )
                self.draw_text_centered(
                    draw, index_box, str(index), self.font, (0, 0, 0, 255)
                )

            pointer += self.CELL_SIZE + self.SPACE

        return img

    def combine_images_vertically(self, images: List[Image]) -> Image:
        max_width = max(img.size[0] for img in images)
        total_height = sum(img.size[1] for img in images)
        final_img = self.create_image((max_width, total_height))

        y_offset = 0
        for img in images:
            final_img.paste(img, (int(max_width / 2 - img.size[0] / 2), y_offset))
            y_offset += img.size[1]

        return final_img

    def img_from_lists(
        self,
        L: List[List[int]],
        highlight_indexes: List[List[int]],
        image_size: Tuple[int, int] = None,
        color=(36, 116, 191, 255),
        highlight_color=(255, 46, 52, 255),
        show_indexes=True,
    ) -> Image:
        imgs = [
            self.img_from_list(
                l,
                hi,
                (image_size[0], int(image_size[1] / len(L))) if image_size else None,
                color,
                highlight_color,
                show_indexes,
            )
            for l, hi in zip(L, highlight_indexes)
        ]
        return self.combine_images_vertically(imgs)

    def img_from_matrix(
        self,
        L: List[List[int]],
        HI: List[List[int]],
        image_size: Tuple[int, int] = None,
        color=(36, 116, 191, 255),
        highlight_color=(255, 46, 52, 255),
        show_indexes=True,
    ) -> Image:
        imgs = [
            self.img_from_list(
                l,
                hi,
                (image_size[0], int(image_size[1] / len(L))) if image_size else None,
                color,
                highlight_color,
                False,
                True,
            )
            for l, hi in zip(L, HI)
        ]
        return self.combine_images_vertically(imgs)
