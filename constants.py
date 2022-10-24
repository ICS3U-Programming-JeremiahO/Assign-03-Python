#!/usr/bin/env python3
# Created By: Jeremiah omoike
# Date: October 19 2022
# This program declares all the constants for my burger program.
# Think of it like a menu because you will find the price for burgers, fries and drink here
HST = 0.13
LABOUR_COST = 2.00
RENTAL_COST = 2.25
INGRED_COST = 1.5
MEDIUM_BURGER = 3.69
LARGE_BURGER = 6.69
DRINK = 1.69
FRIES = 2.19
SUBTOTAL_1 = LABOUR_COST + RENTAL_COST + INGRED_COST * MEDIUM_BURGER
SUBTOTAL_2 = LABOUR_COST + RENTAL_COST + INGRED_COST * LARGE_BURGER
SUBTOTAL_3 = LABOUR_COST + RENTAL_COST + INGRED_COST * MEDIUM_BURGER + FRIES
SUBTOTAL_4 = LABOUR_COST + RENTAL_COST + INGRED_COST * LARGE_BURGER + FRIES
SUBTOTAL_5 = LABOUR_COST + RENTAL_COST + INGRED_COST * MEDIUM_BURGER + FRIES + DRINK
SUBTOTAL_6 = LABOUR_COST + RENTAL_COST + INGRED_COST * LARGE_BURGER + FRIES + DRINK
SUBTOTAL_7 = LABOUR_COST + RENTAL_COST + INGRED_COST * FRIES
SUBTOTAL_8 = LABOUR_COST + RENTAL_COST + INGRED_COST * DRINK
SUBTOTAL_9 = LABOUR_COST + RENTAL_COST + INGRED_COST * DRINK + FRIES
SUBTOTAL_10 = LABOUR_COST + RENTAL_COST + INGRED_COST * MEDIUM_BURGER + DRINK
SUBTOTAL_11 = LABOUR_COST + RENTAL_COST + INGRED_COST * LARGE_BURGER + DRINK
TAX_1 = SUBTOTAL_1 * HST
TAX_2 = SUBTOTAL_2 * HST
TAX_3 = SUBTOTAL_3 * HST
TAX_4 = SUBTOTAL_4 * HST
TAX_5 = SUBTOTAL_5 * HST
TAX_6 = SUBTOTAL_6 * HST
TAX_7 = SUBTOTAL_7 * HST
TAX_8 = SUBTOTAL_8 * HST
TAX_9 = SUBTOTAL_9 * HST
TAX_10 = SUBTOTAL_10 * HST
TAX_11 = SUBTOTAL_11 * HST

TOTAL_1 = SUBTOTAL_1 + TAX_1
TOTAL_2 = SUBTOTAL_2 + TAX_2
TOTAL_3 = SUBTOTAL_3 + TAX_3
TOTAL_4 = SUBTOTAL_4 + TAX_4
TOTAL_5 = SUBTOTAL_5 + TAX_5
TOTAL_6 = SUBTOTAL_6 + TAX_6
TOTAL_7 = SUBTOTAL_7 + TAX_7
TOTAL_8 = SUBTOTAL_8 + TAX_8
TOTAL_9 = SUBTOTAL_9 + TAX_9
TOTAL_10 = SUBTOTAL_10 + TAX_10
TOTAL_11 = SUBTOTAL_11 + TAX_11
