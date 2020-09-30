const { size, chunk } = require("lodash");

const paginationLodash = async (dataList, currentPage, sizePage) => {
  let data = dataList;
  const total = size(data);
  const cutPage = await chunk(data, sizePage);
  const totalPage = cutPage.length;
  if (data.length > 0) {
    data = cutPage[currentPage - 1];
  }

  const pagination = {
    total,
    total_pages: totalPage,
    current_page: currentPage,
    perpage: sizePage,
  };

  return { data, pagination };
};

module.exports = {
  paginationLodash,
};
