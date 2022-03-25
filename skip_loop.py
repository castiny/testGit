import time

intAllItems = 31
# nielsenApp.print_control_identifiers()                
strFileStageStatus = 'not start'
custom_cat_export = [2,6]
retry_cat_export = [4,6]
skip_cat_food = True
originalFile = "ASSORTMENT_REVIEW_804_FOOD_Jan'21.wsv"
modernFile = "ASSORTMENT_REVIEW_804_FOOD_1_Jan'21.wsv"

if (strFileStageStatus == 'custom'):            
    # custom_cat_export = NielsenWinOperations.custom_category_export(strSummaryFilePath,strSummaryFileStage,strSheetFile,strShortName,intAllItems)               
    if (len(custom_cat_export) == 2):
        if (int(custom_cat_export[0]) > 0) and (int(custom_cat_export[0]) < intAllItems) and (int(custom_cat_export[1]) > 0) and (int(custom_cat_export[1]) > int(custom_cat_export[0])) and (int(custom_cat_export[1]) <= intAllItems):
            intStartCategory = int(custom_cat_export[0])
            if ((int(custom_cat_export[1]) + 1) > intAllItems):
                intAllItems = intAllItems
            else:
                intAllItems = (int(custom_cat_export[1]) + 1)
        else:
            # logger().error('start category is zero or stop category is more than total categories or start category more than stop category.')
            print('start category is zero or stop category is more than total categories or start category more than stop category.')
            time.sleep(0.1)
            exit_without_retry = True
            time.sleep(0.1)
            exit_without_retry_msg = "Start category or stop category is invalid."
            time.sleep(0.1)
            exit(0)        
    else:
        if (int(custom_cat_export[0]) > 0):
            if (int(custom_cat_export[0]) < intAllItems):
                intStartCategory = int(custom_cat_export[0])
                if ((int(custom_cat_export[0]) + 1) > intAllItems):
                    intAllItems = intAllItems
                else:
                    intAllItems = intStartCategory + 1
            else:
                # logger().error('custom category more than total categories.')
                print('custom category more than total categories.')
                time.sleep(0.1)
                exit_without_retry = True
                time.sleep(0.1)
                exit_without_retry_msg = "custom category more than total categories."
                time.sleep(0.1)
                exit(0)   
        elif (int(custom_cat_export[0]) == -1):
            intAllItems = intAllItems
        else:
            # logger().error('custom category is zero')
            print('custom category is zero')
            time.sleep(0.1)
            exit_without_retry = True
            time.sleep(0.1)
            exit_without_retry_msg = "custom category is zero"
            time.sleep(0.1)
            exit(0) 
elif (strFileStageStatus == 'fail'):
    # retry_cat_export = NielsenWinOperations.extract_custom_category(strSummaryFilePath,strSummaryFileStage,strSheetFile,strShortName,strFileStageStatus,intAllItems)
    if (len(retry_cat_export) == 2):
        intStartCategory = retry_cat_export[0]
        if (((retry_cat_export[1]) + 1) <= intAllItems):
            intAllItems = retry_cat_export[1] + 1
        else:
            intAllItems = intAllItems
    else:
        intStartCategory = retry_cat_export[0]
        if (((retry_cat_export[0]) + 1) <= intAllItems):
            intAllItems = retry_cat_export[0] + 1
        else:
            intAllItems = intAllItems                                              
else:
    intStartCategory = 1
    intAllItems = intAllItems 
    
# logger().info('intStartCategory: ' + str(intStartCategory))
print('intStartCategory: ' + str(intStartCategory))    
# logger().info('intAllItems: ' + str(intAllItems))
print('intAllItems: ' + str(intAllItems))

