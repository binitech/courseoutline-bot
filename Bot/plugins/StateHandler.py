#####################################################################################
"""                         HANDLING STATES                                       """
#####################################################################################
from Bot import dp
from Bot.helpers import ManageCourse
from Bot.helpers.Database import CsFile
from aiogram import types
from aiogram.dispatcher import FSMContext
from Bot.helpers.ManageCourse import AddMaterialForm, RemoveMaterialForm, DescEditForm, CourseManager, CrhEditForm, \
    FileIdEditForm


@dp.message_handler(state=DescEditForm.code)
async def editDesc(message: types.Message, state: FSMContext):
    if message.text in list(CsFile().get()):
        async with state.proxy() as data:
            data['code'] = message.text
        await message.answer("Now send me the description for this course")
        await DescEditForm.next()
    else:
        await message.answer("The course code you entered is incorrect")


@dp.message_handler(state=DescEditForm.desc)
async def editDesc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        cs = CourseManager()
        cs.edit_desc(c_code=data['code'], value=message.text)
    await message.answer("Description changed successfully")
    await state.finish()


#########################################################################################


@dp.message_handler(state=CrhEditForm.code)
async def editDesc(message: types.Message, state: FSMContext):
    if message.text in list(CsFile().get()):
        async with state.proxy() as data:
            data['code'] = message.text
        await message.answer("Now send me the Credit hour for this course")
        await CrhEditForm.next()
    else:
        await message.answer("The course code you entered is incorrect")


@dp.message_handler(state=CrhEditForm.crh)
async def editDesc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        cs = CourseManager()
        cs.edit_crh(c_code=data['code'], value=message.text)
    await message.answer("Credit hour changed successfully")
    await state.finish()


#########################################################################################


@dp.message_handler(state=FileIdEditForm.code)
async def editDesc(message: types.Message, state: FSMContext):
    if message.text in list(CsFile().get()):
        async with state.proxy() as data:
            data['code'] = message.text
        await message.answer("Now send me the File Id string for this course")
        await FileIdEditForm.next()
    else:
        await message.answer("The course code you entered is incorrect")


@dp.message_handler(state=FileIdEditForm.file)
async def editDesc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        cs = CourseManager()
        cs.edit_fileId(c_code=data['code'], value=message.text)
    await message.answer("File Id String changed successfully")
    await state.finish()

####################################################################################


@dp.message_handler(state=RemoveMaterialForm.code)
async def removeMaterial(message: types.Message, state: FSMContext):
    if message.text in list(CsFile().get()):
        func = ManageCourse.listMaterials(message.text)
        await message.answer(func[0], reply_markup=func[1], parse_mode="MARKDOWN")
        await state.finish()
    else:
        await message.answer("The course code you entered is incorrect")

#####################################################################################


@dp.message_handler(state=AddMaterialForm.code)
async def removeMaterial(message: types.Message, state: FSMContext):
    if message.text in list(CsFile().get()):
        async with state.proxy() as data:
            data['code'] = message.text
        await message.answer("Send me Material Title/Name")
        await AddMaterialForm.next()
    else:
        await message.answer("The course code you entered is incorrect")


@dp.message_handler(state=AddMaterialForm.cName)
async def removeMaterial(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer("Send File string for the material")
    await AddMaterialForm.next()


@dp.message_handler(state=AddMaterialForm.cFile)
async def AddMatCFile(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fileId'] = message.text
    NewMaterial = [data['name'], data['fileId']]
    CourseManager().add_material(data['code'], NewMaterial)
    await message.answer("Material Added Successfully!")
    await state.finish()
