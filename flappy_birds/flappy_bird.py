import pygame

from game_methods import (draw_footer, create_pipe, move_pipe,
						  draw_pipe, check_collision, rotate_bird,
						  bird_animation,score_display)


def main():
	pygame.init()
	screen = pygame.display.set_mode((576,710))
	pygame.display.set_caption('Flappy birds')
	game_font = pygame.font.Font('images/Affirmative.otf',40)
	clock = pygame.time.Clock()
	scale = 0.25
	bird_movement = 0

	# Backgorund
	bg_image = pygame.image.load('images/background-night.png').convert()
	bg_image = pygame.transform.scale2x(bg_image)

	# Footer
	footer_image = pygame.image.load('images/base.png').convert()
	footer_image = pygame.transform.scale2x(footer_image)

	# Bird
	bird_image_midflap = pygame.image.load('images/bird.png').convert_alpha()
	bird_image_midflap = pygame.transform.scale2x(bird_image_midflap)

	bird_image_downflap = pygame.image.load('images/bird_downflap.png').convert_alpha()
	bird_image_downflap = pygame.transform.scale2x(bird_image_downflap)

	bird_image_upflap = pygame.image.load('images/bird_upflap.png').convert_alpha()
	bird_image_upflap = pygame.transform.scale2x(bird_image_upflap)

	bird_list = [bird_image_downflap,bird_image_midflap,bird_image_upflap]
	bird_index = 0
	bird_image = bird_list[bird_index]

	BIRDMAKER = pygame.USEREVENT + 1
	pygame.time.set_timer(BIRDMAKER,200)

	bird_rect = bird_image.get_rect(center=(100,250))

	# Pipe - to`siq
	pipe_image = pygame.image.load('images/pipe.png')
	pipe_image = pygame.transform.scale2x(pipe_image)

	list_pipe = []
	PIPEMAKER = pygame.USEREVENT
	pygame.time.set_timer(PIPEMAKER,1200)

	# game variable
	footer_x_pos = 0
	pipe_height = [250,300,350,400,450]
	game_type = True
	score = 0
	hight_score = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and game_type:
					bird_movement = 0
					bird_movement -= 5
				if event.key == pygame.K_SPACE and game_type == False:
					game_type = True
					list_pipe.clear()
					bird_rect.center = (100,250)
					bird_movement = 0
					score = 0

			if event.type == PIPEMAKER:
				list_pipe.extend(create_pipe(pipe_image,pipe_height))
				#print(list_pipe)
			if event.type == BIRDMAKER:
				if bird_index < 2:
					bird_index += 1
				else:
					bird_index = 0
				bird_image,bird_rect = bird_animation(bird_list,bird_index,bird_rect)
		# backgorund
		screen.blit(bg_image,(0,-350))

		if game_type:
			# Bird
			bird_movement += scale
			rotated_bird = rotate_bird(bird_image,bird_movement)
			bird_rect.centery += bird_movement
			screen.blit(rotated_bird,bird_rect)

			# Pipe - to`siqlar
			list_pipe = move_pipe(list_pipe)
			draw_pipe(screen,pipe_image,list_pipe)

			game_type = check_collision(bird_rect,list_pipe)

			score += 0.01
			score_display(screen,game_font,score,hight_score,"game_active")
		else:
			if score > hight_score:
				hight_score = score
			score_display(screen,game_font,score,hight_score,"game_active")
			

		#Footer
		footer_x_pos -= 1
		draw_footer(screen,footer_image,footer_x_pos)
		if footer_x_pos <= -576:
			footer_x_pos = 0

		pygame.display.update()
		clock.tick(90)


if __name__ == "__main__":
	main() 